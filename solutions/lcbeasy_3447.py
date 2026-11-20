def clearDigits(s: str) -> str:
    st = []
    for c in s:
        if c.isdigit():
            if st:
                st.pop()
        else:
            st.append(c)
    return "".join(st)
