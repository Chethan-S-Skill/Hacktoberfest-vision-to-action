"""
Tests for Database Operations and Isolation.
"""

from database import DatabaseService


def test_database_crud_flow():
    db = DatabaseService()
    test_user_id = "test-user-isolation-01"
    
    # 1. Save an analysis
    sample_response = {
        "visual_observations": ["Burned resistor R1"],
        "interpretation": "Overcurrent failure",
        "threat_level": "CAUTION",
        "next_steps": ["Step 1: Check resistance"],
        "safety_notes": ["Disconnect power"],
        "confidence_score": 90,
    }

    ok, record_id, err = db.save_analysis(
        user_id=test_user_id,
        question="What is wrong with resistor R1?",
        image_path=f"{test_user_id}/test.png",
        ai_response=sample_response,
        threat_level="CAUTION",
    )

    assert ok is True
    assert record_id is not None
    assert err is None

    # 2. Retrieve history for this user
    history = db.get_user_history(user_id=test_user_id)
    assert len(history) >= 1
    found = any(h["id"] == record_id for h in history)
    assert found is True

    # 3. Isolation test: other user cannot see this record
    other_history = db.get_user_history(user_id="other-different-user-99")
    assert not any(h["id"] == record_id for h in other_history)

    # 4. Search filtering
    search_results = db.get_user_history(user_id=test_user_id, search_query="resistor")
    assert len(search_results) >= 1

    # 5. Delete analysis
    del_ok, del_err = db.delete_analysis(record_id, test_user_id)
    assert del_ok is True

    # 6. Verify deleted
    retrieved = db.get_analysis_by_id(record_id, test_user_id)
    assert retrieved is None
