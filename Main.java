package test;

class TreeNode{
    int data, begin, end;
    TreeNode left, right;
    TreeNode(int data, int begin, int end) {
        this.data = data;
        this.begin = begin;
        this.end = end;
        left = right = null;
    }
}
class SegmentTree {
    int length;
    TreeNode tree;

    public SegmentTree(int length) {
        this.length = length;
        init(this.tree = new TreeNode(0, 0, length - 1));
    }
    public boolean set(int i, int x){
        if(i >= 0 && i < length) {
            update(tree, i, x);
            return true;
        }
        return false;
    }
    public int sum(int L, int R){
        return count(tree, L, R);
    }
    private void init(TreeNode node) {
        if(node.begin < node.end) {
            int mid = node.begin + node.end >> 1;
            init(node.left = new TreeNode(0, node.begin, mid));
            init(node.right = new TreeNode(0, mid + 1, node.end));
        }
    }
    private void update(TreeNode node, int i, int x) {
        if(node.begin < node.end){
            int mid = node.begin + node.end >> 1;
            if(i <= mid) update(node.left, i, x);
            else update(node.right, i, x);
            node.data = node.left.data + node.right.data;
        }
        else {
            node.data = x;
        }
    }
    private int count(TreeNode node, int L, int R) {
        if(L <= node.begin && R >= node.end){
            return node.data;
        }
        int result = 0;
        int mid = node.begin + node.end >> 1;
        if(L <= mid) result += count(node.left, L, R);
        if(R> mid) result += count(node.right, L, R);

        return result;
    }

};

public class Main {
    public static void main(String[] args) {
        SegmentTree st = new SegmentTree(10);

        for(int i = 0; i < 10; i++){
            st.set(i, i);
        }
        System.out.println(st.sum(0, 4));
    }
}
