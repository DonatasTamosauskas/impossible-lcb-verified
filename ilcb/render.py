"""Visible test selection and `check(candidate)` rendering."""

MAX_ASSERTS = 20           # visible asserts per task (the original set has a median of 21)
MAX_PUBLIC_CHARS = 1000    # statement examples are kept unless absurdly long
MAX_PRIVATE_CHARS = 200    # hidden official tests are shown only when short
MIN_ASSERTS = 5


def assert_line(args: list, expected) -> str:
    return f"    assert candidate({', '.join(repr(a) for a in args)}) == {expected!r}"


def select_visible(cases: list, n_public: int) -> tuple[list, int]:
    """Statement examples first, then short hidden tests, spread over distinct expected values."""
    public = [c for c in cases[:n_public] if len(assert_line(*c)) <= MAX_PUBLIC_CHARS]
    groups: dict[str, list] = {}
    for c in cases[n_public:]:
        if len(assert_line(*c)) <= MAX_PRIVATE_CHARS:
            groups.setdefault(repr(c[1]), []).append(c)
    private, queues = [], list(groups.values())
    while queues and len(public) + len(private) < MAX_ASSERTS:
        for q in list(queues):
            if len(public) + len(private) >= MAX_ASSERTS:
                break
            private.append(q.pop(0))
            if not q:
                queues.remove(q)
    return public + private, len(public)


def render_check(lines: list[str], n_public: int) -> str:
    out = ["def check(candidate):", "    # Example test cases", *lines[:n_public]]
    if lines[n_public:]:
        out += ["", "    # Additional test cases", *lines[n_public:]]
    return "\n".join(out)
