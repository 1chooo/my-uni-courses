# %% [markdown]
# # [2022 Fall] Assignment4-8
# 
# > Course: AP3021

# %% [markdown]
# ### 4-8
# 
# Read chapter 7.2.2 and explain how to remove a found root of an nth-order polynomial.
# 
# 
# 在迭代數次之後常會發現得到相同的解，因此在我們要進行迭代數次的時候可以從小數點進行著手，以減輕 round-off error 為目標使得結果不會離我們預期的太過遙遠。
# 
# 使 round-off error 不會這麼影響我們的結果，便是要挑選好的估計值，有的時候我們需要從高次項著手，反之我們需要再低次項著手，在好的結果猜想中，所得到的結果可以使我們下次迭代中得到更好的結果，
# 
# 另一種方法是在 deflaction 將獲得的連續根視為良好的初步猜測。然後可以將每個估計值用做初始猜測，再運用 nondeflated polynomial 判定，不過要小心如果兩個 deflacted root 不夠準確以至於收斂至一個解的時候，可能會發生錯誤的誤差發生，此時便要去比對每一個 polished root。
# 
# ##### synthetic division
# ```
# r = a(n)
# a(n) = 0
# DOFOR i = n−1, 0, −1
#     s = a(i)
#     a(i) = r r=s+r*t
# END DO
# ```
# 
# 
# ##### Ploynomial deflaction
# ``` f90
# SUB poldiv(a, n, d, m, q, r) 
#     DOFOR j = 0, n
#         r(j) = a(j)
#         q(j) = 0 
#     END DO
#     DOFOR k = n−m, 0, −1 
#         q(k+1) = r(m+k) ∕ d(m) 
#         DOFOR j = m+k−1, k, −1
#             r(j) = r(j)−q(k+1) * d(j−k) 
#         END DO
#     END DO
#     DOFOR j = m, n
#         r(j) = 0 
#     END DO
#     n = n−m 
# END SUB
# ```

# %%



