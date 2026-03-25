# ==========================================
# STEP 1: DATASET
# ==========================================

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

user_preferences = {
    "preferred_category": "education",
    "preferred_tags": ["ml", "productivity", "archtecture-ai-explained"]
}


# ==========================================
# STEP 2 & 3: RULE-BASED SYSTEM
# ==========================================

def calculate_score(item, user_preferences):
    score = 0

    # Category match
    if item["category"] == user_preferences["preferred_category"]:
        score += 3

    # Tag match
    matching_tags = set(item["tags"]) & set(user_preferences["preferred_tags"])
    score += len(matching_tags) * 2

    # Numeric contribution
    score += item["popularity"] / 50
    score += item["recency"] / 50

    return score


def filter_items(items, user_preferences, min_popularity=0):
    filtered = []

    for item in items:
        if item["popularity"] < min_popularity:
            continue

        category_match = item["category"] == user_preferences["preferred_category"]
        tag_match = len(set(item["tags"]) & set(user_preferences["preferred_tags"])) > 0

        if category_match or tag_match:
            filtered.append(item)

    return filtered


print("\n================ RULE-BASED RECOMMENDATION ================\n")

filtered_items = filter_items(items, user_preferences, min_popularity=80)

scored_items = []

for item in filtered_items:
    score = calculate_score(item, user_preferences)
    scored_items.append((item, score))

scored_items.sort(key=lambda x: x[1], reverse=True)

for item, score in scored_items:
    print(f"{item['title']} → Score: {round(score, 2)}")


# ==========================================
# STEP 4: VECTOR REPRESENTATION
# ==========================================

all_categories = ["programming", "ai", "lifestyle", "education"]

all_tags = [
    "python", "django", "api", "backend",
    "flutter", "mobile", "dart",
    "ml", "ai", "data", "analysis",
    "health", "routine", "wellness",
    "study", "productivity", "focus",
    "deep-learning", "dataset", "archtecture-ai-explained"
]


def item_to_vector(item):
    vector = []

    # Category encoding
    for category in all_categories:
        vector.append(1 if item["category"] == category else 0)

    # Tag encoding
    for tag in all_tags:
        vector.append(1 if tag in item["tags"] else 0)

    # Normalize numeric values
    max_popularity = max(i["popularity"] for i in items)
    max_recency = max(i["recency"] for i in items)

    vector.append(item["popularity"] / max_popularity)
    vector.append(item["recency"] / max_recency)

    return vector


print("\n================ VECTOR REPRESENTATION ================\n")

item_vectors = {}

for item in items:
    vec = item_to_vector(item)
    item_vectors[item["id"]] = vec

    print(item["title"])
    print(vec)
    print()

def user_to_vector(user_preferences):
    vector = []

    for category in all_categories:
        vector.append(1 if user_preferences["preferred_category"] == category else 0)

    for tag in all_tags:
        vector.append(1 if tag in user_preferences["preferred_tags"] else 0)

    return vector


import math

def cosine_similarity(vec1, vec2):
    dot_product = sum(a * b for a, b in zip(vec1, vec2))
    magnitude1 = math.sqrt(sum(a ** 2 for a in vec1))
    magnitude2 = math.sqrt(sum(b ** 2 for b in vec2))

    if magnitude1 == 0 or magnitude2 == 0:
        return 0

    return dot_product / (magnitude1 * magnitude2)


print("\n================ COSINE SIMILARITY RECOMMENDATION ================\n")

user_vector = user_to_vector(user_preferences)

similar_items = []

for item in items:
    item_vector = item_to_vector(item)

    similarity = cosine_similarity(user_vector, item_vector)

    similar_items.append((item, similarity))
    
similar_items.sort(key=lambda x: x[1], reverse=True)

for item, sim in similar_items:
    print(f"{item['title']} → Similarity: {round(sim, 3)}")