import streamlit as st
from streamlit.hashing import _CodeHasher
from streamlit.report_thread import get_report_ctx
from streamlit.server.server import Server

import graphviz as graphviz
from graphviz import Digraph

def main():
    state = _get_state()
    pages = {
        "M=30, K=12": page_st3012,
        "M=28, K=12": page_st2812,
        "M=26, K=12": page_st2612,
        "M=24, K=12": page_st2412,
        "M=30, K=10": page_st3010,
        "M=28, K=8": page_st2808,
        "M=26, K=8": page_st2608,
    }

    st.sidebar.title("Keygraph Parameters")
    st.sidebar.subheader("M= number of black nodes; K=number of red nodes")
    page = st.sidebar.radio("Select values for M and K", tuple(pages.keys()))

    # Display the selected page with the session state
    pages[page](state)

    # Mandatory to avoid rollbacks with widgets, must be called at the end of your app
    state.sync()

def page_st3012(state):
    st.graphviz_chart('''
    graph keygraph {
    graph [size="10,10", overlap="scale"]
    hold [color="black"]
    assemble [color="black"]
    keep [color="black"]
    box [color="black"]
    start [color="black"]
    fold [color="black"]
    price [color="black"]
    set [color="black"]
    easy [color="black"]
    come [color="black"]
    speed [color="black"]
    back [color="black"]
    belt [color="black"]
    issue [color="black"]
    small [color="black"]
    minute [color="black"]
    time [color="black"]
    move [color="black"]
    incline [color="black"]
    put [color="black"]
    far [color="black"]
    product [color="black"]
    even [color="red"]
    hour [color="red"]
    together [color="red"]
    handle [color="red"]
    around [color="red"]
    right [color="red"]
    look [color="red"]
    far--issue
    belt--start
    belt--keep
    belt--speed
    start--speed
    incline--speed
    product--price
    set--easy
    easy--small
    easy--fold
    easy--move
    easy--assemble
    move--fold
    small--fold
    come--box
    come--back
    put--hold
    put--minute
    hold--time
    time--minute
    look--small [color="red", style="dotted"]
    even--speed [color="red", style="dotted"]
    look--price [color="red", style="dotted"]
    handle--fold [color="red", style="dotted"]
    hour--assemble [color="red", style="dotted"]
    hour--time [color="red", style="dotted"]
    handle--hold [color="red", style="dotted"]
    right--belt [color="red", style="dotted"]
    together--easy [color="red", style="dotted"]
    around--easy [color="red", style="dotted"]
    around--move [color="red", style="dotted"]
    together--put [color="red", style="dotted"]
    }
    ''')


def page_st2812(state):
    st.graphviz_chart('''
    graph keygraph {
    graph [size="10,10", overlap="scale"]
    start [color="black"]
    set [color="black"]
    move [color="black"]
    assemble [color="black"]
    issue [color="black"]
    product [color="black"]
    fold [color="black"]
    come [color="black"]
    keep [color="black"]
    easy [color="black"]
    minute [color="black"]
    time [color="black"]
    back [color="black"]
    belt [color="black"]
    hold [color="black"]
    put [color="black"]
    speed [color="black"]
    small [color="black"]
    box [color="black"]
    price [color="black"]
    heavy [color="red"]
    handle [color="red"]
    around [color="red"]
    space [color="red"]
    right [color="red"]
    together [color="red"]
    issue--belt
    start--speed
    start--belt
    speed--belt
    keep--belt
    product--price
    assemble--easy
    easy--small
    easy--fold
    easy--set
    easy--move
    fold--move
    fold--small
    back--come
    come--box
    time--hold
    time--minute
    minute--put
    put--hold
    space--easy [color="red", style="dotted"]
    handle--hold [color="red", style="dotted"]
    space--fold [color="red", style="dotted"]
    heavy--box [color="red", style="dotted"]
    heavy--easy [color="red", style="dotted"]
    right--belt [color="red", style="dotted"]
    heavy--move [color="red", style="dotted"]
    together--easy [color="red", style="dotted"]
    around--easy [color="red", style="dotted"]
    space--small [color="red", style="dotted"]
    around--move [color="red", style="dotted"]
    together--put [color="red", style="dotted"]
    }
    ''')

def page_st2612(state):
    st.graphviz_chart('''
    graph keygraph {
    graph [size="10,10", overlap="scale"]
    small [color="black"]
    minute [color="black"]
    product [color="black"]
    speed [color="black"]
    box [color="black"]
    put [color="black"]
    hold [color="black"]
    back [color="black"]
    easy [color="black"]
    price [color="black"]
    fold [color="black"]
    come [color="black"]
    start [color="black"]
    belt [color="black"]
    time [color="black"]
    move [color="black"]
    together [color="red"]
    set [color="red"]
    heavy [color="red"]
    space [color="red"]
    right [color="red"]
    assemble [color="red"]
    around [color="red"]
    keep [color="red"]
    product--price
    start--speed
    start--belt
    belt--speed
    small--fold
    small--easy
    easy--fold
    easy--move
    fold--move
    come--box
    come--back
    minute--put
    minute--time
    put--hold
    time--hold
    space--fold [color="red", style="dotted"]
    heavy--easy [color="red", style="dotted"]
    keep--belt [color="red", style="dotted"]
    right--belt [color="red", style="dotted"]
    heavy--move [color="red", style="dotted"]
    together--easy [color="red", style="dotted"]
    around--easy [color="red", style="dotted"]
    space--small [color="red", style="dotted"]
    set--easy [color="red", style="dotted"]
    around--move [color="red", style="dotted"]
    assemble--easy [color="red", style="dotted"]
    together--put [color="red", style="dotted"]
    }
    ''')

def page_st2412(state):
    st.graphviz_chart('''
    graph keygraph {
    graph [size="10,10", overlap="scale"]
    product [color="black"]
    back [color="black"]
    assemble [color="black"]
    hold [color="black"]
    belt [color="black"]
    easy [color="black"]
    start [color="black"]
    come [color="black"]
    time [color="black"]
    issue [color="black"]
    price [color="black"]
    set [color="black"]
    put [color="black"]
    small [color="black"]
    move [color="black"]
    speed [color="black"]
    fold [color="black"]
    handle [color="red"]
    hour [color="red"]
    minute [color="red"]
    around [color="red"]
    together [color="red"]
    keep [color="red"]
    space [color="red"]
    belt--issue
    belt--start
    belt--time
    belt--speed
    start--speed
    time--speed
    product--price
    assemble--easy
    easy--small
    easy--fold
    easy--set
    easy--move
    small--fold
    move--fold
    back--come
    back--put
    hold--put
    hour--time [color="red", style="dotted"]
    minute--put [color="red", style="dotted"]
    space--easy [color="red", style="dotted"]
    handle--hold [color="red", style="dotted"]
    space--fold [color="red", style="dotted"]
    keep--belt [color="red", style="dotted"]
    minute--time [color="red", style="dotted"]
    together--easy [color="red", style="dotted"]
    around--easy [color="red", style="dotted"]
    space--small [color="red", style="dotted"]
    around--move [color="red", style="dotted"]
    together--put [color="red", style="dotted"]
    }
    ''')


def page_st3010(state):
    st.graphviz_chart('''
    graph keygraph {
    graph [size="10,10", overlap="scale"]
    hold [color="black"]
    price [color="black"]
    far [color="black"]
    product [color="black"]
    assemble [color="black"]
    start [color="black"]
    minute [color="black"]
    speed [color="black"]
    small [color="black"]
    put [color="black"]
    box [color="black"]
    come [color="black"]
    time [color="black"]
    back [color="black"]
    easy [color="black"]
    fold [color="black"]
    incline [color="black"]
    set [color="black"]
    issue [color="black"]
    belt [color="black"]
    move [color="black"]
    keep [color="black"]
    even [color="red"]
    look [color="red"]
    right [color="red"]
    handle [color="red"]
    together [color="red"]
    hour [color="red"]
    far--issue
    incline--speed
    belt--start
    belt--keep
    belt--speed
    start--speed
    product--price
    small--fold
    small--easy
    easy--fold
    easy--set
    easy--move
    easy--assemble
    fold--move
    back--come
    box--come
    hold--put
    hold--time
    time--minute
    put--minute
    look--small [color="red", style="dotted", dir=none]
    even--speed [color="red", style="dotted", dir=none]
    look--price [color="red", style="dotted", dir=none]
    handle--fold [color="red", style="dotted", dir=none]
    hour--assemble [color="red", style="dotted", dir=none]
    hour--time [color="red", style="dotted", dir=none]
    handle--hold [color="red", style="dotted", dir=none]
    right--belt [color="red", style="dotted", dir=none]
    together--easy [color="red", style="dotted", dir=none]
    together--put [color="red", style="dotted", dir=none]
    }
    ''')


def page_st2808(state):
    st.graphviz_chart('''
    graph keygraph {
    graph [size="10,10", overlap="scale"]
    keep [color="black"]
    put [color="black"]
    minute [color="black"]
    box [color="black"]
    speed [color="black"]
    belt [color="black"]
    back [color="black"]
    easy [color="black"]
    move [color="black"]
    start [color="black"]
    fold [color="black"]
    price [color="black"]
    product [color="black"]
    issue [color="black"]
    hold [color="black"]
    time [color="black"]
    assemble [color="black"]
    set [color="black"]
    come [color="black"]
    small [color="black"]
    together [color="red"]
    space [color="red"]
    heavy [color="red"]
    around [color="red"]
    right [color="red"]
    keep--belt
    speed--start
    speed--belt
    belt--issue
    belt--start
    product--price
    assemble--easy
    move--fold
    move--easy
    set--easy
    easy--small
    easy--fold
    fold--small
    back--come
    box--come
    time--hold
    time--minute
    hold--put
    put--minute
    heavy--easy [color="red", style="dotted"]
    right--belt [color="red", style="dotted"]
    heavy--move [color="red", style="dotted"]
    together--easy [color="red", style="dotted"]
    around--easy [color="red", style="dotted"]
    space--small [color="red", style="dotted"]
    around--move [color="red", style="dotted"]
    together--put [color="red", style="dotted"]
    }
    ''')

def page_st2608(state):
    st.graphviz_chart('''
    graph keygraph {
    graph [size="10,10", overlap="scale"]
    start [color="black"]
    speed [color="black"]
    product [color="black"]
    hold [color="black"]
    time [color="black"]
    back [color="black"]
    easy [color="black"]
    small [color="black"]
    price [color="black"]
    come [color="black"]
    fold [color="black"]
    move [color="black"]
    minute [color="black"]
    put [color="black"]
    box [color="black"]
    belt [color="black"]
    assemble [color="red"]
    space [color="red"]
    together [color="red"]
    around [color="red"]
    set [color="red"]
    right [color="red"]
    product--price
    start--speed
    start--belt
    speed--belt
    move--fold
    move--easy
    easy--small
    easy--fold
    small--fold
    box--come
    back--come
    minute--put
    minute--time
    time--hold
    put--hold
    right--belt [color="red", style="dotted"]
    together--easy [color="red", style="dotted"]
    around--easy [color="red", style="dotted"]
    space--small [color="red", style="dotted"]
    set--easy [color="red", style="dotted"]
    around--move [color="red", style="dotted"]
    assemble--easy [color="red", style="dotted"]
    together--put [color="red", style="dotted"]
    }
    ''')


class _SessionState:

    def __init__(self, session, hash_funcs):
        """Initialize SessionState instance."""
        self.__dict__["_state"] = {
            "data": {},
            "hash": None,
            "hasher": _CodeHasher(hash_funcs),
            "is_rerun": False,
            "session": session,
        }

    def __call__(self, **kwargs):
        """Initialize state data once."""
        for item, value in kwargs.items():
            if item not in self._state["data"]:
                self._state["data"][item] = value

    def __getitem__(self, item):
        """Return a saved state value, None if item is undefined."""
        return self._state["data"].get(item, None)
        
    def __getattr__(self, item):
        """Return a saved state value, None if item is undefined."""
        return self._state["data"].get(item, None)

    def __setitem__(self, item, value):
        """Set state value."""
        self._state["data"][item] = value

    def __setattr__(self, item, value):
        """Set state value."""
        self._state["data"][item] = value
    
    def clear(self):
        """Clear session state and request a rerun."""
        self._state["data"].clear()
        self._state["session"].request_rerun()
    
    def sync(self):
        """Rerun the app with all state values up to date from the beginning to fix rollbacks."""

        # Ensure to rerun only once to avoid infinite loops
        # caused by a constantly changing state value at each run.
        #
        # Example: state.value += 1
        if self._state["is_rerun"]:
            self._state["is_rerun"] = False
        
        elif self._state["hash"] is not None:
            if self._state["hash"] != self._state["hasher"].to_bytes(self._state["data"], None):
                self._state["is_rerun"] = True
                self._state["session"].request_rerun()

        self._state["hash"] = self._state["hasher"].to_bytes(self._state["data"], None)


def _get_session():
    session_id = get_report_ctx().session_id
    session_info = Server.get_current()._get_session_info(session_id)

    if session_info is None:
        raise RuntimeError("Couldn't get your Streamlit Session object.")
    
    return session_info.session


def _get_state(hash_funcs=None):
    session = _get_session()

    if not hasattr(session, "_custom_session_state"):
        session._custom_session_state = _SessionState(session, hash_funcs)

    return session._custom_session_state


if __name__ == "__main__":
    main()
