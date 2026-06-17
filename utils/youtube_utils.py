import urllib.parse

def create_youtube_search_link(query):
    encoded = urllib.parse.quote(query)

    return (
        f"https://www.youtube.com/results?search_query={encoded}"
    )

def parse_youtube_courses(youtube_text):

    lines = youtube_text.split("\n")

    current_course = {}
    courses = []

    for line in lines:

        line = line.strip()

        if not line:
            continue

        if (
            len(line) > 2
            and line[0].isdigit()
            and "." in line
        ):

            if current_course:
                courses.append(current_course)

            current_course = {
                "course": line.split(".", 1)[1].strip()
            }

        elif line.startswith("Channel:"):

            current_course["channel"] = (
                line.replace("Channel:", "")
                .strip()
            )

        elif line.startswith("Search Query:"):

            current_course["query"] = (
                line.replace("Search Query:", "")
                .strip()
            )

    if current_course:
        courses.append(current_course)

    return courses