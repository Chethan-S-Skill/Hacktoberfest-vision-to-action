"""
Tests for AI Engine and Structured Parsing.
"""

from ai_engine import AIEngine, DEMO_PRESETS


def test_ai_engine_presets_integrity():
    engine = AIEngine()
    for key in ["circuit_burn", "industrial_flowchart", "hydraulic_leak", "appliance_motherboard"]:
        preset = engine.get_preset(key)
        assert preset is not None
        assert "title" in preset
        assert "response" in preset
        resp = preset["response"]
        assert "visual_observations" in resp
        assert "interpretation" in resp
        assert "threat_level" in resp
        assert "next_steps" in resp
        assert "safety_notes" in resp
        assert "uncertainty" in resp
        assert "confidence_score" in resp


def test_parse_structured_json():
    engine = AIEngine()
    valid_json = """
    ```json
    {
      "visual_observations": ["Red wire connected to pin 1", "LED unlit"],
      "interpretation": "Open circuit detected.",
      "threat_level": "LOW",
      "confidence_score": 90,
      "next_steps": ["Step 1: Inspect switch"],
      "safety_notes": ["Verify power switch is off"],
      "uncertainty": ["Wire termination occluded"],
      "follow_up_questions": ["What is battery voltage?"]
    }
    ```
    """
    parsed = engine._parse_structured_response(valid_json)
    assert parsed["threat_level"] == "LOW"
    assert parsed["confidence_score"] == 90
    assert len(parsed["visual_observations"]) == 2
    assert len(parsed["next_steps"]) == 1


def test_defensive_plain_text_parsing():
    engine = AIEngine()
    plain_text = "I observe a burned capacitor with scorch marks. High voltage hazard present. 1. Disconnect AC power. 2. Discharge capacitor."
    parsed = engine._parse_structured_response(plain_text)
    assert parsed["threat_level"] == "CAUTION"
    assert len(parsed["next_steps"]) >= 1
    assert parsed["confidence_score"] > 0


def test_empty_question_handling():
    engine = AIEngine()
    res = engine.analyze_image(b"fake_bytes", "")
    assert res["success"] is False
    assert "Please provide a question" in res["error"]


def test_fallback_flowchart_detection():
    engine = AIEngine()
    resp = engine._generate_fallback_analysis("Can you explain this logic flowchart?")
    assert "Process Start" in str(resp["visual_observations"])
