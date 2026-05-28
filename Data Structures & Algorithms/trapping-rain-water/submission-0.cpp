class Solution {
public:
    int trap(vector<int>& height) {
        stack<int> st;
        int n = height.size();
        long long ans=0;
        for(int i=0;i<n;++i){
            if(height[i]==0) continue;
            int last = 0;
            while(!st.empty()){
                int t = st.top();
                if(height[t]<=height[i]){
                    ans += (height[t]-last)*(i-t-1);
                    last = height[t];
                    st.pop();
                }
                else break;
            }
            
            if(!st.empty()) ans+=(height[i]-last)*(i-st.top()-1);
            // cout<<ans<<"\n";
            st.push(i);
        }
        return ans;
    }
};
