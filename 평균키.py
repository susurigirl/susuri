# π¨ μ¬κΈ°λ κ·Έλλ‘ π
heights = input("νμλ€μ ν€λ₯Ό μλ ₯νμΈμ\n").split()
# split() => κΈ°λ³Έκ³΅λ°±(μ€νμ΄μ€)λ‘ μλ ₯λ κ°μ λ¦¬μ€νΈλ‘ μ μ₯
# print(heights)
for n in range(0, len(heights)):  # ν€μ μ«μλ§νΌ λ°λ³΅
    heights[n] = int(heights[n])  # λ¬Έμμ΄ λ¦¬μ€νΈλ₯Ό μ«μ λ¦¬μ€νΈλ‘ κ΅μ²΄
print(heights)
# π¨ μ¬κΈ°λ κ·Έλλ‘ π

# μλμ μ½λ μμ± π

total_height = 0
for h in heights:
    total_height += h
print(f"μ μ²΄ ν€μ ν© = {total_height}")
print(f"νμ±μ μ«μλ {len(heights)}")
print(f"νκ·  ν€μ κ°μ : {total_height/len(heights)}")
