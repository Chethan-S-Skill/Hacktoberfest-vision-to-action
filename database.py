"""
Database Service for Reality -> Action AI.
Manages PostgreSQL CRUD operations on the 'analysis_history' table with RLS enforcement.
Includes a local persisted JSON fallback for standalone demo operation.
"""

import os
import json
import uuid
from datetime import datetime, timezone
from typing import List, Dict, Any, Optional, Tuple
from utils.config import get_config
from auth import get_supabase_client
from storage import StorageService

LOCAL_DB_FILE = os.path.join("temp_images", "local_history.json")


class DatabaseService:
    def __init__(self, force_local: bool = False):
        self.config = get_config()
        self.force_local = force_local
        self.client = None if force_local else get_supabase_client()
        self.storage = StorageService()
        self._init_local_db()

    @property
    def is_live(self) -> bool:
        return self.client is not None and not self.force_local

    def _init_local_db(self):
        if not os.path.exists("temp_images"):
            os.makedirs("temp_images", exist_ok=True)
        if not os.path.exists(LOCAL_DB_FILE):
            try:
                with open(LOCAL_DB_FILE, "w", encoding="utf-8") as f:
                    json.dump([], f)
            except Exception:
                pass

    def _read_local_db(self) -> List[Dict[str, Any]]:
        try:
            with open(LOCAL_DB_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return []

    def _write_local_db(self, records: List[Dict[str, Any]]):
        try:
            with open(LOCAL_DB_FILE, "w", encoding="utf-8") as f:
                json.dump(records, f, indent=2)
        except Exception:
            pass

    def save_analysis(
        self,
        user_id: str,
        question: str,
        image_path: Optional[str],
        ai_response: Dict[str, Any],
        threat_level: str = "LOW",
        model_name: str = "sarvam-gemma-4",
    ) -> Tuple[bool, Optional[str], Optional[str]]:
        """
        Saves a completed analysis record.
        Returns: (success: bool, record_id: Optional[str], error_message: Optional[str])
        """
        if not user_id or not question or not ai_response:
            return False, None, "User ID, question, and AI response are required to save analysis."

        record_id = str(uuid.uuid4())
        created_at = datetime.now(timezone.utc).isoformat()

        if not self.is_live:
            records = self._read_local_db()
            new_record = {
                "id": record_id,
                "user_id": user_id,
                "question": question,
                "image_path": image_path,
                "ai_response": ai_response,
                "model_name": model_name,
                "threat_level": threat_level,
                "status": "completed",
                "created_at": created_at,
            }
            records.insert(0, new_record)
            self._write_local_db(records)
            return True, record_id, None

        try:
            payload = {
                "id": record_id,
                "user_id": user_id,
                "question": question,
                "image_path": image_path,
                "ai_response": ai_response,
                "model_name": model_name,
                "threat_level": threat_level,
                "status": "completed",
                "created_at": created_at,
            }
            res = self.client.table("analysis_history").insert(payload).execute()
            if res.data:
                return True, record_id, None
            return False, None, "Database insert returned empty result."
        except Exception as e:
            return False, None, f"Database error: {str(e)}"

    def get_user_history(
        self,
        user_id: str,
        limit: int = 50,
        search_query: Optional[str] = None,
    ) -> List[Dict[str, Any]]:
        """Retrieves history for the current authenticated user only."""
        if not user_id:
            return []

        if not self.is_live:
            records = [r for r in self._read_local_db() if r.get("user_id") == user_id]
            if search_query:
                q = search_query.strip().lower()
                records = [
                    r for r in records
                    if q in r.get("question", "").lower()
                    or q in str(r.get("ai_response", {})).lower()
                ]
            return records[:limit]

        try:
            query = (
                self.client.table("analysis_history")
                .select("*")
                .eq("user_id", user_id)
                .order("created_at", desc=True)
                .limit(limit)
            )
            if search_query:
                query = query.ilike("question", f"%{search_query.strip()}%")
            res = query.execute()
            return res.data or []
        except Exception:
            return []

    def get_analysis_by_id(self, analysis_id: str, user_id: str) -> Optional[Dict[str, Any]]:
        """Retrieves a single analysis by ID, strictly verifying ownership."""
        if not analysis_id or not user_id:
            return None

        if not self.is_live:
            for r in self._read_local_db():
                if r.get("id") == analysis_id and r.get("user_id") == user_id:
                    return r
            return None

        try:
            res = (
                self.client.table("analysis_history")
                .select("*")
                .eq("id", analysis_id)
                .eq("user_id", user_id)
                .single()
                .execute()
            )
            return res.data
        except Exception:
            return None

    def delete_analysis(self, analysis_id: str, user_id: str) -> Tuple[bool, Optional[str]]:
        """Deletes an analysis record and its associated private stored image."""
        if not analysis_id or not user_id:
            return False, "Analysis ID and user ID are required."

        record = self.get_analysis_by_id(analysis_id, user_id)
        if not record:
            return False, "Record not found or unauthorized."

        # Delete image from storage if path exists
        image_path = record.get("image_path")
        if image_path:
            self.storage.delete_image(image_path)

        if not self.is_live:
            records = [r for r in self._read_local_db() if r.get("id") != analysis_id]
            self._write_local_db(records)
            return True, None

        try:
            self.client.table("analysis_history").delete().eq("id", analysis_id).eq("user_id", user_id).execute()
            return True, None
        except Exception as e:
            return False, f"Failed to delete record: {str(e)}"
