from rest_framework.decorators import api_view
from rest_framework.response import Response
from .services import call_llm


@api_view(["POST"])
def process_request(request):

    try:
        data = request.data

        # STEP 6 → Validation
        if not data:
            return Response({
                "status": "error",
                "message": "No data provided"
            }, status=400)

        age = data.get("age")

        if age is None:
            return Response({
                "status": "error",
                "message": "Age field is required"
            }, status=400)

        age = int(age)

        # STEP 8 → Simple Logic
        risk = "High" if age > 50 else "Low"

        # STEP 9 → LLM Integration
        report = data.get("report", "")
        prompt = f"Simplify this medical report: {report}"

        llm_result = call_llm(prompt)

        result = {
            "risk_level": risk,
            "ai_output": llm_result
        }

        return Response({
            "status": "success",
            "data": result
        })

    except Exception:
        return Response({
            "status": "error",
            "message": "Internal server error"
        }, status=500)