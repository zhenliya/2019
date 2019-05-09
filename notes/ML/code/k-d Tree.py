"""https://www.cnblogs.com/eyeszjwang/articles/2429382.html
https://leileiluoluo.com/posts/kdtree-algorithm-and-implementation.html


 维度为k，数据点数为N的数据集，k-d tree适用于N>=2^k的情形
一个平衡的k-d tree，其所有叶子节点到根节点的距离近似相等。但一个平衡的k-d tree对最近邻搜索、空间搜索等应用场景并非是最优的。
常规的k-d tree的构建过程为：循环依序取数据点的各维度来作为切分维度，取数据点在该维度的中值作为切分超平面，
将中值左侧的数据点挂在其左子树，将中值右侧的数据点挂在其右子树。递归处理其子树，直至所有数据点挂载完毕。
"""
# d-tree构建代码
def kd_tree(points, depth):
    if 0 == len(points):
        return None
    cutting_dim = depth % len(points[0])
    medium_index = len(points) // 2
    points.sort(key=itemgetter(cutting_dim))
    node = Node(points[medium_index])
    node.left = kd_tree(points[:medium_index], depth + 1)
    node.right = kd_tree(points[medium_index + 1:], depth + 1)
    return node

    # 寻找d维最小坐标值点代码
    def findmin(n, depth, cutting_dim, min):
    if min is None:
        min = n.location
    if n is None:
        return min
    current_cutting_dim = depth % len(min)
    if n.location[cutting_dim] < min[cutting_dim]:
        min = n.location
    if cutting_dim == current_cutting_dim:
            return findmin(n.left, depth + 1, cutting_dim, min)
    else:
        leftmin = findmin(n.left, depth + 1, cutting_dim, min)
        rightmin = findmin(n.right, depth + 1, cutting_dim, min)
        if leftmin[cutting_dim] > rightmin[cutting_dim]:
            return rightmin
        else:
            return leftmin
# 新增节点
def insert(n, point, depth):
    if n is None:
        return Node(point)
    cutting_dim = depth % len(point)
    if point[cutting_dim] < n.location[cutting_dim]:
        if n.left is None:
            n.left = Node(point)
        else:
            insert(n.left, point, depth + 1)
    else:
        if n.right is None:
            n.right = Node(point)
        else:
            insert(n.right, point, depth + 1)

# 为平衡树结构，删除节点
def delete(n, point, depth):
    cutting_dim = depth % len(point)
    if n.location == point:
        if n.right is not None:
            n.location = findmin(n.right, depth + 1, cutting_dim, None)
            delete(n.right, n.location, depth + 1)
        elif n.left is not None:
            n.location = findmin(n.left, depth + 1)
            delete(n.left, n.location, depth + 1)
            n.right = n.left
            n.left = None
        else:
            n = None
    else:
        if point[cutting_dim] < n.location[cutting_dim]:
            delete(n.left, point, depth + 1)
        else:
            delete(n.right, point, depth + 1)