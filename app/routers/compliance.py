from fastapi import APIRouter
from pydantic import BaseModel, HttpUrl, Field
from datetime import datetime, timezone
import sys
from pathlib import Path

# Ensure the skills directory is in sys.path to import from .antigravity
skills_path = str(Path(__file__).parent.parent.parent / ".antigravity" / "skills")
if skills_path not in sys.path:
    sys.path.append(skills_path)

from compliance_tools import calculate_risk

router = APIRouter(prefix="/compliance", tags=["compliance"])

class ComplianceRequest(BaseModel):
    # Rule: exactly 8 characters long
    realtor_license_id: str = Field(..., min_length=8, max_length=8, description="License ID must be exactly 8 characters.")
    image_url: HttpUrl
    is_structural_change: bool
    # Rule: ge=0 and le=1
    ai_confidence_score: float = Field(..., ge=0, le=1)

@router.post("/verify-image")
async def verify_image(request: ComplianceRequest):
    # Use the skill to calculate risk
    risk_rating = calculate_risk(request.ai_confidence_score, request.is_structural_change)
    
    return {
        "realtor_license_id": request.realtor_license_id,
        "risk_rating": risk_rating,
        "timestamp": datetime.now(timezone.utc).isoformat()
    }
