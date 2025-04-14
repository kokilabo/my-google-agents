import datetime
from zoneinfo import ZoneInfo
from google.adk.agents import Agent

def get_weather(city: str) -> dict:
    """指定された都市の現在の天気情報を取得します。
    
    Args:
        city (str): 天気情報を取得する都市の名前。
    
    Returns:
        dict: ステータスと結果またはエラーメッセージ。
    """
    if city.lower() == "東京":
        return {
            "status": "success",
            "report": (
                "東京の天気は晴れで、気温は25度です。"
            ),
        }
    else:
        return {
            "status": "error",
            "error_message": f"'{city}'の天気情報は利用できません。",
        }

def get_current_time(city: str) -> dict:
    """指定された都市の現在の時刻を返します。
    
    Args:
        city (str): 現在時刻を取得する都市の名前。
    
    Returns:
        dict: ステータスと結果またはエラーメッセージ。
    """
    
    if city.lower() == "東京":
        tz_identifier = "Asia/Tokyo"
    else:
        return {
            "status": "error",
            "error_message": (
                f"{city}のタイムゾーン情報がありません。"
            ),
        }
    
    tz = ZoneInfo(tz_identifier)
    now = datetime.datetime.now(tz)
    report = (
        f'{city}の現在時刻は{now.strftime("%Y-%m-%d %H:%M:%S %Z%z")}です'
    )
    return {"status": "success", "report": report}

root_agent = Agent(
    name="weather_time_agent",
    model="gemini-2.0-flash",
    description=(
        "都市の時間と天気に関する質問に答えるエージェント。"
    ),
    instruction=(
        "都市の時間と天気に関する質問に答えることができます。"
    ),
    tools=[get_weather, get_current_time],
)
