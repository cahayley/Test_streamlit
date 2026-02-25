import streamlit as st

st.set_page_config(
    page_title="Tic Tac Toe",
    page_icon="❌",
    layout="centered",
)

st.title("❌ Tic Tac Toe")

# Initialize session state
if "board" not in st.session_state:
    st.session_state.board = [""] * 9
if "player" not in st.session_state:
    st.session_state.player = "X"
if "winner" not in st.session_state:
    st.session_state.winner = None


def check_winner(board):
    win_patterns = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
        (0, 4, 8), (2, 4, 6)              # Diagonals
    ]

    for a, b, c in win_patterns:
        if board[a] == board[b] == board[c] and board[a] != "":
            return board[a]

    if "" not in board:
        return "Draw"

    return None


def make_move(index):
    if st.session_state.board[index] == "" and st.session_state.winner is None:
        st.session_state.board[index] = st.session_state.player
        st.session_state.winner = check_winner(st.session_state.board)
        st.session_state.player = "O" if st.session_state.player == "X" else "X"


# Display board
cols = st.columns(3)

for i in range(9):
    with cols[i % 3]:
        st.button(
            st.session_state.board[i] if st.session_state.board[i] != "" else " ",
            key=i,
            on_click=make_move,
            args=(i,),
            use_container_width=True,
        )

# Display result
if st.session_state.winner:
    if st.session_state.winner == "Draw":
        st.info("It's a Draw! 🤝")
    else:
        st.success(f"Player {st.session_state.winner} Wins! 🎉")
else:
    st.write(f"Current Turn: **{st.session_state.player}**")

# Reset button
if st.button("🔄 Restart Game"):
    st.session_state.board = [""] * 9
    st.session_state.player = "X"
    st.session_state.winner = None