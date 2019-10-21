def findPassword(a) :
    Header = 0 #헤더를 가리키는 변수
    result = [] # 최종 출력 결과를 나타내는 리스트
    for i in range(len(a)) : # 입력 받은 결과 만큼 진행
        # < 가 나오면 헤더 1 감소
        if a[i] is '<' :
            if(Header == 0) :
                continue
            else :
                Header -= 1
        # > 가 나오면 헤더 1 증가
        elif a[i] is '>' :
            if(Header >= len(result)) :
                continue
            else :
                Header += 1
        # 헤더가 0이 아닐 경우 삭제
        elif a[i] == '-' :
            if(Header == 0) :
                continue
            else :
                Header -= 1
                result.pop(Header)
        # 헤더 위치에 문자 넣기
        else:
            result.insert(Header, a[i])
            Header += 1

    return result

if __name__ == "__main__" :
    # T = int(input())

    # for _ in range(T) :
    #     a = input()
    #     print(''.join(findPassword(a)))
    print(''.join(findPassword("<<BP<A>>Cd-")))
    print(''.join(findPassword("f<->--><-l>>d---u-j><>-<u->xb<<axkh<-wk>k>--t--s<b<i<ir>--ey>t>>sx<-yb<>jw<-qaruwy<osnshf><<<-uzz--<")))
    # axwkieybtsbybqaruwosnuhfywx
    print(''.join(findPassword("f<->--><-l>>d---u-j><>-<u->xb<<a")))