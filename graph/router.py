from graph.state import GraphState


def routing_condition(state: GraphState):

    if state["ingestion_mode"] == "resume":

        return "resume_parser"

    return "manual_input"