int select(int arr[], int i)
{
    int j, minIndex, temp;
    minIndex = i;
    for (j = i + 1; j < sizeof(arr) / sizeof(arr[0]); j++)
    {
        if (arr[j] < arr[minIndex])
            minIndex = j;
    }
    temp = arr[minIndex];
    arr[minIndex] = arr[i];
    arr[i] = temp;
    return 0;
}

void selectionSort(int arr[], int n)
{
    int i, j, minIndex, temp;
    for (i = 0; i < n - 1; i++)
    {
        minIndex = i;
        for (j = i + 1; j < n; j++)
        {
            if (arr[j] < arr[minIndex])
                minIndex = j;
        }
        temp = arr[minIndex];
        arr[minIndex] = arr[i];
        arr[i] = temp;
    }
}