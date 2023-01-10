void countSwaps(vector<int> a) {
    int n = a.size();
    int numSwaps = 0;
    for(int i = 0; i < n; i++) {
        for(int j = 0; j < n-1; j++) {
            if(a[j] > a[j+1]) {
                swap(a[j], a[j+1]);
                numSwaps++;
            }
        }
    }
    cout << "Array is sorted in " << numSwaps << " swaps." << endl;
    cout << "First Element: " << a[0] << endl;
    cout << "Last Element: " << a[n-1] << endl;
}