lst = ['ATAGA','ATC','GAT']

# 最重要的是助教提醒的结构：{0: {'A': 1}, 1: {'B': 2, 'C': 4}, 2: {'D': 3}}。按照网上的那都是
# {‘A'：{'T':'G'}}这样的结构，完全不知道怎么输出node的数字节点

# with open("dataset.txt", "r") as f:  # 打开文件
#     lst = f.read().split("\n")
# print(lst)
Trie = {}
count = 0

cur_node = 0
Trie[cur_node] = {}

for patterns in lst:
    cur_node = 0  # 这里需要置0是因为从新的patterns开始就是从root的0检查
    # print("patterns", patterns)
    # print("Trie[cur_node]", Trie[cur_node])
    for currentSymbol in patterns: # currentSymbol是字母，是在edge上的
        # print("currentSymbol", currentSymbol)
        # print("cur_node", cur_node)
        # print("Trie.get(cur_node,"")", Trie.get(cur_node,"xxxxsss"))
        if currentSymbol in Trie.get(cur_node,"xxxxsss"):  # 如果能找到这个节点，那就顺着往下走，不需要创建新的节点
            # 这里假如直接写Trie[cur_node]则可能因为没有cur_node而报错。
            # 用get则默认找不到的情况下返回xxxxsss（也就是乱设的）的值，注意不能包含ATGC，否则会被if认为包含。当然，要是不包含，返回
            # xxxxsss那肯定是不会有currentSymbol的
            cur_node = Trie[cur_node][currentSymbol]  # 如果包含这个节点，则能够直接取Trie[cur_node]。
            # print("cur_node1", cur_node)
        else:  # 这个else就是要创建新节点了
            if Trie.get(cur_node,"xxsss") == 'xxsss':  # 这种情况是之前完全没有并列的节点，从新创造，比如最开始的ABCD
                Trie[cur_node] = {currentSymbol: (1+count)} # 这里应该是增加进去，而不是替换进去
                cur_node += 1  # 这个if也只对应ABCD这样往下一直走，每次也都是加一
                # print("run1")
            else:  # 这种情况是有并列的，比如ABC和ABD，C与D就是并列
                # cur_node = count
                Trie[cur_node][currentSymbol] = 1+count  # 在else里说明能找到cur_node，则可以创建内层字典。
                # 每次创建新节点都是数字最大的，所以用count，尝试发现应该加一
                # print("run2")
                cur_node = count + 1  # 走到currentSymbol的末端节点
                # print("Trie[cur_node]_set", Trie[cur_node])
                # 检查这里，这里应该让count增加才对，但是缺少了这一步，似乎是要在什么条件下把最大值，也就是count，赋予给此处的cur_node?
            # print("cur_node2", cur_node)
            # print("Trie", Trie)
        if count < cur_node:
            count = cur_node  # 永远存储最大的步值
#         print("count", count)
#     print("TIRE", Trie)
print(Trie)

# with open("test.txt", "w") as f:
#     for key in Trie:
#         # print(Trie[key])
#         for key1 in Trie[key]:
#             f.write(f"{key}->{Trie[key][key1]}:{key1}\n")

