import java.util.Scanner;

//import com.sun.corba.se.impl.orbutil.graph.Node;

class TreeNode {
	long data, lazy;
	int begin, end;
    TreeNode left, right;

    TreeNode(long data, int begin, int end) {
        this.lazy = 0;
        this.data = data;
        this.begin = begin;
        this.end = end;
        left = right = null;
    }
}

class SegmentTree {
    int length;
    TreeNode tree;

    private void init(TreeNode node) {
        if (node.begin < node.end) {
            int mid = node.begin + node.end >> 1;
            init(node.left = new TreeNode(0, node.begin, mid));
            init(node.right = new TreeNode(0, mid + 1, node.end));
        }
    }

    private void updateLazy(TreeNode node) {
        if (node.begin < node.end) {
            node.left.lazy += node.lazy;
            node.right.lazy += node.lazy;
        }

        node.data += (node.end - node.begin + 1) * node.lazy;
        node.lazy = 0;
    }

    private long addBatch(TreeNode node, int L, int R, int x) {
        if (L <= node.begin && R >= node.end) {
            node.lazy += x;
        }

        if (node.lazy != 0) {
            updateLazy(node);
        }

        if (L > node.end || R < node.begin) {
            return node.data;
        }

        if (L <= node.begin && R >= node.end) {
            return node.data;
        }

        long result = 0;
        result += addBatch(node.left, L, R, x);
        result += addBatch(node.right, L, R, x);

        return node.data = result;
    }

    private long countWithLazy(TreeNode node, int L, int R) {
        if (node.lazy != 0) {
            updateLazy(node);
        }

        if (L > node.end || R < node.begin) {
            return 0;
        }

        if (L <= node.begin && R >= node.end) {
            return node.data;
        }

        long result = 0;
        result += countWithLazy(node.left, L, R);
        result += countWithLazy(node.right, L, R);

        return result;
    }

    public SegmentTree(int length) {
        this.length = length;
        init(this.tree = new TreeNode(0, 0, length - 1));
    }

    public boolean add(int L, int R, int x) {
        if (L >= tree.begin && R <= tree.end) {
            addBatch(tree, L, R, x);
            return true;
        }

        return false;
    }

    public long sum(int L, int R) {
        return countWithLazy(tree, L, R);
    }
}

public class Main {
    public static void main(String[] args) {
    	Scanner sc = new Scanner(System.in);
    	int N, Q;
    	N = sc.nextInt();
    	Q = sc.nextInt();
        SegmentTree st = new SegmentTree(N);
        
        for (int i = 0; i < N; i++) {
        	int x;
        	x = sc.nextInt();
            st.add(i, i, x);
        }
        for(int i = 0; i < Q; i++) {
        	java.lang.String s = sc.next();
        	char c = s.charAt(0);
        	if(c == 'Q') {
        		int l, r;
        		l = sc.nextInt();
        		r = sc.nextInt();
        		System.out.println(st.sum(l - 1, r - 1));
        	}
        	else {
        		int l, r, x;
        		l = sc.nextInt();
        		r = sc.nextInt();
        		x = sc.nextInt(); 
       			st.add(l - 1, r - 1, x);
        	}
        }
    }
}





