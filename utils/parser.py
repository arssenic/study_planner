def parse_output(output):

    study_idx = output.find("## STUDY TABLE")
    phase_idx = output.find("## PHASES")
    tips_idx = output.find("## SUCCESS_TIPS")
    resource_idx = output.find("## RESOURCES")
    youtube_idx = output.find("## YOUTUBE_COURSES")

    if min(
        study_idx,
        phase_idx,
        tips_idx,
        resource_idx,
        youtube_idx
    ) == -1:

        return None

    return {
        "table": output[study_idx:phase_idx],
        "phases": output[phase_idx:tips_idx],
        "tips": output[tips_idx:resource_idx],
        "resources": output[resource_idx:youtube_idx],
        "youtube": output[youtube_idx:]
    }