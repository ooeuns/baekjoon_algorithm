#include <iostream>
using namespace std;

int main(){
    int c, n, sum=0, up=0;			// 테스트케이스 c, 학생의 수 n, 평균이 넘는 학생들 카운팅 up.
	double *score, print, avg=0;	// 학생들 점수 score, 출력을 위한 변수, 평균 점수 avg.

	cin >> c;

	for (int i=0; i < c; i++) {
		cin >> n;			// 학생의 수 파악
		score = new double[n];	// 학생의 수 만큼 점수 입력을 위한 배열 생성.

        sum=0;
		for (int j = 0; j < n; j++) {
			cin >> score[j];	// 점수 입력 받음.
			sum += score[j];	// 입력 받은 점수 다 더하기.
		}
		avg = sum / n;	// 학생의 수로 나눠주기. (산술평균 구하기)

        up=0;
		for (int k = 0; k < n; k++) {
			if (avg < score[k]) {	// 평균 보다 높은 점수의 학생수 카운팅.
				up++;
			}
		}

        cout << fixed;
		cout.precision(3);
    	cout << (double)up / (double)n * 100<<"%"<<endl;
	}
	return 0;
}
