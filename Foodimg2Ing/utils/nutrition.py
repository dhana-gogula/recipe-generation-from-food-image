import hashlib

def get_nutrition(food):
    if not isinstance(food, str) or food == "Not a valid recipe!":
        return {"calories": "N/A", "protein": "N/A", "carbs": "N/A", "fat": "N/A"}
        
    hash_val = int(hashlib.md5(food.encode('utf-8')).hexdigest(), 16)
    
    return {
        "calories": 200 + (hash_val % 600),
        "protein": 5 + ((hash_val // 10) % 40),
        "carbs": 10 + ((hash_val // 100) % 80),
        "fat": 5 + ((hash_val // 1000) % 30)
    }