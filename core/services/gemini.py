from google import genai
from django.conf import settings
import json
from google.genai import types


PROMPT = """
You are an expert agronomist and soil scientist helping Georgian farmers. 
Analyze the soil image provided and return a JSON response (ONLY JSON, no markdown, no explanation outside JSON).

The JSON must have this exact structure:
{
  "healthScore": <number 0-100>,
  "status": <"კარგი" | "საშუალო" | "ცუდი">,
  "statusLevel": <"good" | "warning" | "bad">,
  "color": "<soil color in Georgian, e.g. მუქი ყავისფერი>",
  "colorSub": "<what it indicates, short, Georgian>",
  "texture": "<texture type, Georgian, e.g. თიხნარი>",
  "textureSub": "<brief implication, Georgian>",
  "moisture": "<moisture level, Georgian, e.g. ზომიერი>",
  "moistureSub": "<brief note, Georgian>",
  "analysis": "<3-4 paragraph detailed analysis in Georgian. Cover: soil color and what it means, texture and structure, visible organic matter, potential pH range, crop suitability, any problems spotted>",
  "recommendations": [
    {"icon": "🌱", "text": "<recommendation in Georgian>", "priority": <"high"|"medium"|"low">},
    {"icon": "💧", "text": "<recommendation in Georgian>", "priority": <"high"|"medium"|"low">},
    {"icon": "🧪", "text": "<recommendation in Georgian>", "priority": <"high"|"medium"|"low">}
  ]
}

Be specific and practical. If the image is not soil, say so in the analysis and set healthScore to 0.
Always respond in Georgian language. Return ONLY the JSON object.;
"""

def analyze_soil(image_file):
    client = genai.Client(api_key=settings.GEMINI_API_KEY)

    response = client.models.generate_content(
        model = "gemini-3.6-flash",
        contents = [PROMPT,
            types.Part.from_bytes(
                data = image_file.read(),
                mime_type=image_file.content_type,
            ),
        ],
    )

    return json.loads(response.text)