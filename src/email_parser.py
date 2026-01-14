import base64


def get_plain_text_body(message):
    payload = message.get("payload", {})
    parts = payload.get("parts", [])

    # If email has no parts (simple text email)
    if not parts:
        body = payload.get("body", {}).get("data")
        if body:
            return base64.urlsafe_b64decode(body).decode("utf-8")
        return ""

    # If email has multiple parts
    for part in parts:
        mime_type = part.get("mimeType")
        body = part.get("body", {}).get("data")

        if mime_type == "text/plain" and body:
            return base64.urlsafe_b64decode(body).decode("utf-8")

    return ""
