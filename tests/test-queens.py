from src.queens import solve_n_queens

def test_n4():
    res = solve_n_queens(4)
    assert len(res) == 2

def test_n8():
    res = solve_n_queens(8)
    assert len(res) == 92

if __name__ == "__main__":
    test_n4()
    test_n8()
    print("测试通过")
