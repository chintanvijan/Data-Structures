#include<iostream.h>
#include<conio.h>

int binary_search(int arr[],int start_index,int end_index,int x){
	int size = end_index-start_index;
	int mid ;
	if(size%2==0){
		mid = size/2;
	}
	else{
		mid = (size+1)/2;
	}
	if(x==arr[mid]){
		return mid;
	}
	else if(x<arr[mid]){
		binary_search(arr,start_index,mid,x);
	}
	else if(x>arr[mid]){
		binary_search(arr,mid+1,end_index,x);
	}

}

void main(){
	int arr[20],n,x,t,i,j;
	clrscr();
	cout<<"Enter size of array :";
	cin>>n;
	cout<<"Enter elements of array :";
	for(i=0;i<n;i++){
	   cin>>arr[i];
	}
	cout<<"Enter Element to be searched for:";
	cin>>x;

       cout<< binary_search(arr,0,n,x);
	getch();
}