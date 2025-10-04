import streamlit as st

st.title("🎮 لعبة XO - Tic Tac Toe")

if "board" not in st.session_state:
    st.session_state.board = [["" for _ in range(3)] for _ in range(3)]
if "turn" not in st.session_state:
    st.session_state.turn = "X"
if "winner" not in st.session_state:
    st.session_state.winner = None

def check_winner(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != "":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != "":
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != "":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != "":
        return board[0][2]
    return None

if st.button("🔄 إعادة تشغيل اللعبة"):
    st.session_state.board = [["" for _ in range(3)] for _ in range(3)]
    st.session_state.turn = "X"
    st.session_state.winner = None

cols = st.columns(3)
for r in range(3):
    for c in range(3):
        cell = st.session_state.board[r][c] or " "
        if cols[c].button(cell, key=f"{r}-{c}"):
            if not st.session_state.winner and st.session_state.board[r][c] == "":
                st.session_state.board[r][c] = st.session_state.turn
                winner = check_winner(st.session_state.board)
                if winner:
                    st.session_state.winner = winner
                else:
                    st.session_state.turn = "O" if st.session_state.turn == "X" else "X"

if st.session_state.winner:
    st.success(f"🎉 الفائز: {st.session_state.winner}")
else:
    st.write(f"الدور على: {st.session_state.turn}")
