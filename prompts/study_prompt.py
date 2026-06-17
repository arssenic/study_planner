def generate_prompt(subject, days, hours_per_day, current_level):

    return f"""
You are an elite academic coach.

Create a study plan for:

Subject: {subject}
Duration: {days} days
Daily Hours: {hours_per_day}
Level: {current_level}

Return EXACTLY in this format:

## STUDY TABLE

| Day | Focus Topic | Core Milestone Activity | Active Recall Checkpoint Question |
|-----|-------------|-------------------------|-----------------------------------|

## PHASES

### Foundation Phase (Days X-Y)
Explanation

### Deep Dive Phase (Days A-B)
Explanation

### Practice Phase (Days C-D)
Explanation

## SUCCESS_TIPS

1. Tip
2. Tip
3. Tip
4. Tip
5. Tip

## RESOURCES

### can be Books or websites anything that is relevant to the subject

## YOUTUBE_COURSES

Recommend exactly 5 YouTube courses/playlists.

For each provide:

- Course Name
- Instructor/Channel Name
- YouTube Search Query

Example:

1. Striver A2Z DSA Course
   Channel: take U forward
   Search Query: Striver A2Z DSA Course

2. Data Structures Full Course
   Channel: freeCodeCamp
   Search Query: Data Structures Full Course freeCodeCamp

Rules:
- Generate exactly ONE markdown table.
- Do not repeat table headers.
Generate exactly {days} rows.
"""