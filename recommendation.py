items = [
    {
        "id": 1,
        "title": "Learn Django Basics",
        "category": "programming",
        "tags": ["python", "django", "backend"],
        "popularity": 90,
        "recency": 80,
    },
    {
        "id": 2,
        "title": "Flutter for Beginners",
        "category": "programming",
        "tags": ["flutter", "mobile", "dart"],
        "popularity": 85,
        "recency": 70,
    },
    {
        "id": 3,
        "title": "Advanced Machine Learning",
        "category": "ai",
        "tags": ["ml", "ai", "python"],
        "popularity": 95,
        "recency": 60,
    },
    {
        "id": 4,
        "title": "Healthy Morning Routine",
        "category": "lifestyle",
        "tags": ["health", "routine", "wellness"],
        "popularity": 75,
        "recency": 85,
    },
    {
        "id": 5,
        "title": "Build REST APIs with Django",
        "category": "programming",
        "tags": ["django", "api", "backend"],
        "popularity": 88,
        "recency": 78,
    },
    {
        "id": 6,
        "title": "Intro to Data Science",
        "category": "ai",
        "tags": ["data", "python", "analysis"],
        "popularity": 80,
        "recency": 72,
    },
    {
        "id": 7,
        "title": "Productivity Tips for Students",
        "category": "education",
        "tags": ["study", "productivity", "focus"],
        "popularity": 70,
        "recency": 90,
    },
    {
        "id": 8,
        "title": "Neural Networks Explained",
        "category": "ai",
        "tags": ["ai", "ml", "deep-learning"],
        "popularity": 92,
        "recency": 65,
    },
    {
        "id": 9,
        "title": "AI things explained from scratch",
        "category": "ai",
        "tags": ["ml", "dataset", "archtecture-ai-explained"],
        "popularity": 922,
        "recency": 625,
    },
]

for item in items:
    print(item)
    
user_preferences = {
    "preferred_category": "programming",
    "preferred_tags": ["python", "django", "api"]
}

def calculate_score(item, user_preferences):
    score = 0

    # 1. Category match
    if item["category"] == user_preferences["preferred_category"]:
        score += 3

    # 2. Tag match
    matching_tags = set(item["tags"]) & set(user_preferences["preferred_tags"])
    score += len(matching_tags) * 2

    # 3. Popularity contribution
    score += item["popularity"] / 50

    # 4. Recency contribution
    score += item["recency"] / 50

    return score

scored_items = []

for item in items:
    score = calculate_score(item, user_preferences)
    scored_items.append((item, score))
    
scored_items.sort(key=lambda x: x[1], reverse=True)

print("\nRecommended Items:\n")

for item, score in scored_items:
    print(f"{item['title']} → Score: {round(score, 2)}")