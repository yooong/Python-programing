class Member:
    def __init__(self,name=0,id=0,password=0,profile=0):
        self.name=name
        self.id=id
        self.password=password
        self.profile=profile
        self.member_info_list=[] #회원 정보를 저장하기 위한 빈 리스트
        self.member_info_dict={} #회원 정보를 저장하기 위한 빈 딕셔너리
        self.dict_value=[] #회원 정보 딕셔너리에 value값을 넣기 위한 빈 리스트
        self.id_list=[] #ID를 저장하기 위한 빈 리스트
        self.pw_list=[] #비밀번호를 저장하기 위한 빈 리스트
        self.login_id="" #로그인 후, 로그인 된 ID를 저장하기 위한 변수
        self.login_pw="" #로그인 후, 로그인 된 비밀번호를 저장하기 위한 변수
        self.writer="" #타임라인글 작성 시 작성자를 표시하기 위한 변수
        self.time="" #타임라인글 작성 시 시간을 표시하기 위한 변수
        self.writing="" #타임라인글 작성 시 타임라인글을 표시하기 위한 변수
        self.tag=[] #타임라인글 작성 시 태그 항목을 표시하기 위한 변수
        self.serial_number="" #타임라인글 작성 시 고유번호를 저장하기 위한 변수
        self.serial_number_list=[] #고유번호를 저장하기 위한 리스트
        self.timeline_dict={} #타임라인글의 내용(고유번호, 작성자, 시간 등)을 저장하기 위한 빈 딕셔너리
        self.timeline_value=[] #타임라인 딕셔너리의 value값을 넣기 위한 빈 리스트
        self.good=0 #타임라인글의 처음 좋아요 개수
        self.chat=[] #타임라인글의 댓글
        self.chat_dict={} #타임라인글의 댓글 딕셔너리
        global id_list #회원이 아닐 때 로그인할 경우, 조건에 쓰기 위한 리스트
        id_list=[]

    def create_member(self): #회원가입
        print("<회 원 가 입>")
        print("")
        self.name=input("이름: ")
        print("")
        self.id=input("ID: ")
        print("")
        while self.id in self.id_list: #회원가입 시 중복된 ID를 허용하지 않게
            self.id=input("중복된 ID입니다. 다시 입력해주세요: ")
            print("")
        self.password=input("비밀번호: ")
        print("")
        self.profile=input("프로필: ")
        print("")
        self.id_list.append(self.id) #ID를 리스트에 저장(회원가입 시 이 리스트에 입력한 ID가 있으면 안 됨.)
        self.pw_list.append(self.password) #비밀번호를 리스트에 저장
        id_list.append(self.id) #회원이 없는 경우 / 있는 경우를 나눠서 지정하기 위해 리스트에 저장해 줌
        blank=[]
        blank.append(self.name)
        blank.append(self.id)
        blank.append(self.password)
        blank.append(self.profile)
        self.member_info_list.append(blank) #회원 정보(이름, ID, 비밀번호, 프로필)를 리스트에 저장
        blank=[]
        blank.append(self.name)
        blank.append(self.password)
        blank.append(self.profile)
        self.dict_value.append(blank) #ID를 딕셔너리의 key로 하기 위해 value로 넣을 이름, 비밀번호, 프로필 리스트 생성
        self.member_info_dict=dict.fromkeys(self.id_list) #ID를 회원 정보 딕셔너리의 key로
        for i in range(len(self.id_list)):  #위에서 저장한 value를 회원 정보 딕셔너리의 value로
            self.member_info_dict[self.id_list[i]]=self.dict_value[i]
        print("<회 원 가 입 완 료>")
        print("-"*120)

    def login(self): #로그인
        print("<로 그 인>")
        print("")
        self.login_id=input("ID: ") #로그인할 ID 입력
        print("")
        self.login_pw=input("비밀번호: ") #로그인할 ID의 비밀번호 입력
        print("")
        if len(self.id_list)==0: #회원이 아무도 없는 경우(회원가입을 하도록 유도)
            print("존재하지 않는 회원입니다. 로그인을 원하시면 회원가입을 해주세요.")
            print("-"*120)
        else: #
            global login_again #ID와 비밀번호가 일치하지 않을 때 조건으로 사용하기 위한 변수
            login_again=1 #초기값 설정
            if self.login_id in self.member_info_dict and self.login_pw==self.member_info_dict[self.login_id][1]:
                login_again=0 # 나중에 while문에서 나오기 위한 설정(1이 아닌 아무 값)
                print("<로 그 인 완 료>")  #입력한 ID가 회원 정보 딕셔너리에 있고 입력한 비밀번호가 입력한 ID의 비밀번호와 일치하면 로그인이 되게
                print("-"*120)
            elif self.login_id not in self.member_info_dict or self.login_pw != self.member_info_dict[self.login_id][1]:
                print("ID 또는 비밀번호를 확인해주세요. 로그인 메뉴로 이동합니다.")
                print("-"*120)  #입력한 ID가 회원 정보 딕셔너리에 없거나 입력한 비밀번호가 입력한 ID의 비밀번호와 일치하지 않을 때

    def update_member_info(self): #회원 정보 수정
        print("<회 원 정 보 수 정>")
        print("")
        print("ID는 수정할 수 없습니다.")
        print("")
        for i in range(len(self.member_info_list)):
            if self.login_id in self.member_info_list[i][1]: #본인의 회원 정보만 변경할 수 있게(단, ID는 변경 불가)
                self.member_info_list[i][0]=input("이름: ") #변경할 이름
                self.member_info_list[i][2]=input("비밀번호: ") #변경할 비밀번호
                self.member_info_list[i][3]=input("프로필: ") #변경할 프로필
                self.pw_list[i]=self.member_info_list[i][2] #비밀번호를 바꾸는 경우 앞에서 생성한 비밀번호 리스트에 저장된 비밀번호도 바꿔 줌
                self.login_pw=self.member_info_list[i][2] #비밀번호를 바꾸는 경우 로그인한 비밀번호도 바꿔 줌
            else: #나머지는 그대로 유지
                self.member_info_list[i]=self.member_info_list[i]
        print("")
        print("회 원 정 보 수 정 완 료>")
        print("-"*120)

    def show_member_info(self): #회원 정보 열람
        print("<회 원 정 보 열 람>")
        print("")
        for i in range(len(self.member_info_list)): #모든 회원의 정보 열람
            print("회원"+str(i+1))
            for j in range(len(self.member_info_list[i])):
                if j==0:
                    print("")
                    print("이름: "+self.member_info_list[i][j])
                elif j==1:
                    print("")
                    print("ID: "+self.member_info_list[i][j])
                elif j==2:
                    print("")
                    print("비밀번호: 비밀번호는 열람할 수 없습니다.") #비밀번호는 열람할 수 없게
                else:
                    print("")
                    print("프로필: "+self.member_info_list[i][j])
            print("")
            print("*"*40)
            print("")

        print("<회 원 정 보 열 람 완 료>")
        print("-"*120)

    def remove_member(self): #회원 탈퇴
        print("<회 원 탈 퇴>")
        print("")
        answer=input("정말로 회원 탈퇴를 원하시나요?(복구 불가) [yes/no]: ") #한 번 더 묻기
        print("-"*120)
        if answer=="yes":
            for i in range(len(self.member_info_list)):
                if self.login_id in self.member_info_list[i][1]: #본인이 로그인한 ID를 탈퇴하게
                    del self.member_info_list[i] #회원 정보 리스트에서도 삭제
                    del id_list[i] #ID 리스트에서도 삭제
                    del self.member_info_dict[self.id_list[i]]
                    del self.id_list[i]
                    del self.pw_list[i]
                    break
                else:
                    self.member_info_list[i]=self.member_info_list[i] #나머지 회원의 정보는 그대로

            print("")
            print("<회 원 탈 퇴 완 료>")
            print("")
            print("로그인 메뉴로 돌아갑니다.")
            print("-"*120)
        else:
            print("")
            print("<회 원 탈 퇴 취 소>")
            print("")
            print("로그인 메뉴로 돌아갑니다.")
            print("-"*120)

    def input_timeline(self): #타임라인글 작성
        print("<타 임 라 인 작 성>")
        print("")
        from datetime import datetime
        self.serial_number=input("원하는 고유번호(숫자)를 입력해주세요: ")
        print("")
        while self.serial_number in self.serial_number_list: #고유번호가 중복되지 않게
            self.serial_number=input("중복된 고유번호입니다. 다시 입력해주세요: ")
        self.serial_number_list.append(self.serial_number) #고유번호의 중복을 막기 위해 리스트에 고유번호 저장
        time=datetime.now() #현재 시각 저장
        self.time="%d년 %d월 %d일 %d시 %d분 %d초"%(time.year,time.month,time.day,time.hour,time.minute,time.second) #게시 시간
        self.writer=self.login_id #작성자
        self.writing=input("타임라인글 작성: ") #타임라인글
        print("")
        self.tag=input("태그항목 입력(여러 개면 스페이스바로 구분해주세요): ").split(" ") #태그 항목
        print("")
        self.chat_dict=dict.fromkeys(self.serial_number_list)
        for i in range(len(self.chat_dict)):
            self.chat_dict[self.serial_number_list[i]]=[]
        self.timeline_dict=dict.fromkeys(self.serial_number_list) #고유번호를 key로 하는 타임라인 딕셔너리 생성
        timeline=[]
        for i in [self.writer,self.time,self.writing,self.tag,self.good]: #타임라인 딕셔너리의 value를 리스트에 저장
            timeline.append(i)
        self.timeline_value.append(timeline)
        for i in range(len(self.serial_number_list)): #위에서 저장한 value 리스트를 딕셔너리의 value로 하여 타임라인 딕셔너리 생성
            self.timeline_dict[self.serial_number_list[i]]=self.timeline_value[i]
        print("<타 임 라 인 작 성 완 료>")
        print("-"*120)

    def remove_timeline(self): #타임라인글 삭제
        print("<타 임 라 인 글 삭 제>")
        print("")
        if len(self.timeline_dict)==0: #타임라인에 글이 없는 경우
            print("삭제할 수 있는 타임라인글이 없습니다.")
            print("-"*120)
        else: #타임라인에 글이 있는 경우
            n=input("삭제하고 싶은 타임라인글의 고유번호를 입력해주세요: ")
            print("")
            if n not in self.timeline_dict: #고유번호가 존재하지 않는 경우(=존재하지 않는 글인 경우)
                print("존재하지 않는 글입니다.")
                print("-"*120)
            elif self.login_id != self.timeline_dict[n][0] and n in self.timeline_dict: #고유번호는 존재하지만 본인의 글이 아닌 경우
                print("다른 회원의 타임라인글은 삭제할 수 없습니다.")
                print("-"*120)
            elif self.login_id==self.timeline_dict[n][0] and n in self.timeline_dict: #고유번호도 존재하고 본인이 작성한 글인 경우(삭제)
                del self.timeline_dict[n] #타임라인 딕셔너리에서 삭제
                del self.chat_dict[n]
                del self.timeline_value[self.serial_number_list.index(n)] #타임라인 딕셔너리의 밸류값에서도 삭제
                del self.serial_number_list[self.serial_number_list.index(n)] #고유번호 리스트에서 삭제한 타임라인글의 고유번호 삭제
                print("<삭 제 완 료>")
                print("-"*120)

    def add_good_response(self): #좋아요 누르기
        print("<좋 아 요>")
        print("")
        if len(self.timeline_dict)==0: #타임라인에 글이 없는 경우
            print("좋아요를 누를 수 있는 타임라인글이 없습니다.")
            print("-"*120)
        else: #타임라인에 글이 있는 경우
            n=input("좋아요를 누르고 싶은 글의 고유번호를 입력해주세요: ") #고유번호를 이용하여 좋아요 누르기
            print("")
            if n not in self.timeline_dict: #고유번호가 존재하지 않는 경우(=존재하지 않는 글인 경우)
                print("존재하지 않는 글입니다.")
                print("-"*120)
            else:
                if self.login_id==self.timeline_dict[n][0]: #좋아요를 누르려는 글이 본인의 글인 경우(좋아요를 누르지 못 하게)
                    print("본인의 글에는 좋아요를 누를 수 없습니다.")
                    print("-"*120)
                else:
                    self.timeline_dict[n][4]+=1 #글의 고유번호가 입력될 때마다 타임라인 딕셔너리의 좋아요 개수가 늘어나게
                    print(self.timeline_dict[n][0]+": "+"감사합니다!") #좋아요를 받은 작성자의 감사인사
                    print("-"*120)

    def input_chat(self): #댓글 쓰기
        print("<댓 글 입 력>")
        print("")
        if len(self.timeline_dict)==0: #타임라인글 이 없는 경우
            print("댓글을 쓸 수 있는 타임라인글이 없습니다.")
            print("-"*120)
        else:
            n=input("댓글을 쓰고 싶은 글의 고유번호를 입력해주세요: ")
            print("")
            if n not in self.timeline_dict: #타임라인글은 있지만 존재하지 않는 글을 선택한 경우
                print("존재하지 않는 글입니다.")
                print("-"*120)
            else: #댓글 쓰기
                chat=input("댓 글: ")
                chat2=self.member_info_dict[self.login_id][0]+": "+chat #로그인된 아이디(댓글을 다는 사람): 댓글내용
                self.chat_dict[n].append(chat2) #입력된 댓글을 타임라인 딕셔너리의 value 중 댓글 리스트에 저장
                print("")
                print("<댓 글 입 력 완 료>")
                print("-"*120)

    def show_timeline(self):
        print("<타 임 라 인 목 록>")
        print("")
        if len(self.timeline_dict)==0:
            print("*"*50)
            print("")
            print("타임라인이 없습니다.")
            print("")
            print("*"*50)
            print("-"*120)
        else:
            for i in range(len(self.timeline_dict)-1,-1,-1): #타임라인글의 정보가 먼저 입력한 순으로 저장되기 때문에 거꾸로 출력(가장 최신 글이 위로 가게)
                print("*"*50)
                print("")
                print("고유번호: "+self.serial_number_list[i])
                for j in range(len(self.timeline_dict[self.serial_number_list[i]])+1):
                    if j==0:
                        print("")
                        print("작성자: "+self.timeline_dict[self.serial_number_list[i]][j])
                        print("")
                    elif j==1:
                        print("작성 시간: "+self.timeline_dict[self.serial_number_list[i]][j])
                        print("")
                    elif j==2:
                        print("작성 내용: "+self.timeline_dict[self.serial_number_list[i]][j])
                        print("")
                    elif j==3:
                        for k in range(len(self.timeline_dict[self.serial_number_list[i]][j])):
                            print("#"+self.timeline_dict[self.serial_number_list[i]][j][k]+" ",end="")
                    elif j==4:
                        print("")
                        print("")
                        print("좋아요 개수: "+str(self.timeline_dict[self.serial_number_list[i]][j]))
                    elif j==5:
                        print("")
                        print("댓글 개수: "+str(len(self.chat_dict[self.serial_number_list[i]])))
                        for k in range(len(self.chat_dict[self.serial_number_list[i]])):
                            print("ㄴ"+self.chat_dict[self.serial_number_list[i]][k])
                print("*"*50)
            print("-"*120)

def print_login_menu(): #여러번 반복되는 코드라서 함수로 정의함
    print("<로 그 인 메 뉴>")
    print("")
    print("1. 로그인")
    print("")
    print("2. 회원가입")
    print("")
    print("3. 프로그램 종료")
    print("")
    global select
    select=input("메 뉴 선 택(숫자): ") #메뉴를 숫자로 선택하게
    print("-"*120)
#####################프로그램 시작#######################
a=Member()
print_login_menu()
while select not in ["1","2","3"]: #메뉴를 잘못 선택했을 때(1, 2, 3이 아닌 다른 값을 입력했을 때)다시 선택하게 하기
    select=input("다시 입력해주세요(1~3): ")
    print("-"*120)
while select=="2": #회원가입을 선택한 경우
    a.create_member() #회원가입 메뉴
    print_login_menu() #회원가입 후 다시 로그인 메뉴로 돌아옴
    while select not in ["1","2","3"]: #회원가입 후에도 메뉴를 잘못 선택했을 때 다시 입력하게 하기
        select=input("다시 입력해주세요(1~3): ")
        print("-"*120)
if select=="1": #로그인을 선택한 경우
    while len(id_list)==0: #회원이 없는 경우에 다시 로그인 메뉴로 돌아가기 위한 코드
        a.login() #로그인을 먼저 시도함(시도하게 되면 실패 메세지가 출력됨)
        print_login_menu() #다시 로그인 메뉴로 돌아옴
        while select not in ["1","2","3"]: #이 경우에도 메뉴를 잘못 선택했을 때(1, 2, 3이 아닌 다른 값을 입력했을 때)다시 선택하게 하기
            select=input("다시 입력해주세요(1~3): ")
            print("-"*120)
        while select=="2": #회원가입을 선택한 경우
            a.create_member() #회원가입 메뉴
            print_login_menu() #회원가입 후 다시 로그인 메뉴로 돌아옴
        if select=="3": #프로그램 종료를 선택한 경우
            any=1 #임의로 any라는 값을 지정
        if any==1: break #any가 1이면(=프로그램 종료를 선택허면) 회원이 없는 경우에 돌아가는 while문을 종료함
    login_again=1 #위의 login메서드에서 지정한 변수의 초기값 설정
    while len(id_list)!=0 and login_again==1: #회원은 존재하지만 ID 또는 비밀번호가 틀린 경우에 다시 로그인 메뉴로 돌아가기 위한 코드
        a.login() #로그인을 시도함
        if login_again==0: break #login메서드에서 로그인을 성공하면 login_again=0이 되도록 설정해 놓았음. 따라서 로그인이 성공하면 while문을 종료함
        print_login_menu() #로그인에 성공하지 못했을 경우 다시 로그인 메뉴로 돌아옴
        while select not in ["1","2","3"]: #이 경우에도 메뉴를 잘못 선택했을 때(1, 2, 3이 아닌 다른 값을 입력했을 때)다시 선택하게 하기
            select=input("다시 입력해주세요(1~3): ")
            print("-"*120)
        while select=="2": #회원가입을 선택한 경우
            a.create_member() #회원가입 메뉴
            print_login_menu() #회원가입 후 다시 로그인 메뉴로 돌아옴
        if select=="3": #프로그램 종료를 선택한 경우
            any=1
        if any==1: break
    if any==1: #any가 1인 경우(두 개의 while문 에서 하나라도 프로그램 종료를 선택한 경우 종료 메세지 출력 후 프로그램 종료)
        print("")
        print("<프 로 그 램 종 료>")
        print("-"*120)
    elif login_again==0: #로그인을 성공한 경우
        a.show_timeline() #타임라인 목록 출력
        print("<메 인 메 뉴>") #메인 메뉴 목록 출력
        print("")
        menu=["1. 본인 회원 정보 수정","2. 타임라인글 작성 및 게시","3. 타임라인글 삭제",
              "4. 다른 회원의 타임라인글에 좋아요","5. 타임라인글에 댓글","6. 다른 회원 정보 열람",
              "7. 회원탈퇴","8. 로그아웃","9. 프로그램 종료"]
        for i in menu:
            print(i)
            print("")
        menu_s=input("메 뉴 선 택(숫자): ") #메뉴를 숫자로 입력하게
        print("-"*120)
        while menu_s not in ["1","2","3","4","5","6","7","8","9"]: #메인 메뉴를 잘못 선택했을 때(1~9가 아닌 다른 값을 입력 했을 경우) 다시 선택하게 하기
            print("")
            menu_s=input("다시 입력해주세요(1~9): ")
            print("-"*120)
        while menu_s not in ["7","8","9"]: #로그아웃 또는 프로그램 종료를 선택하지 않은 경우 선택한 메뉴 실행 후 다시 메뉴를 고를 수 있게 메뉴로 돌아오는 코드
            if menu_s=="1": #본인 회원 정보 수정
                a.update_member_info()
            elif menu_s=="2": #타임라인글 작성 및 게시
                a.input_timeline()
            elif menu_s=="3": #타임라인글 삭제
                a.remove_timeline()
            elif menu_s=="4": #다른 회원의 타임라인글에 좋아요
                a.add_good_response()
            elif menu_s=="5": #타임라인글에 댓글
                a.input_chat()
            elif menu_s=="6": #다른 회원 정보 열람
                a.show_member_info()
            a.show_timeline()
            print("<메 인 메 뉴>")
            print("")
            for i in menu:
                print(i)
                print("")
            menu_s=input("메 뉴 선 택(숫자): ")
            print("-"*120)
        while menu_s=="7" or menu_s=="8": #회원탈퇴 또는 로그아웃 후 다시 로그인 메뉴로 돌아가는 코드(이후 진행 방식은 앞의 진행 방식과 동일)
            ######################회원탈퇴 또는 로그아웃 이후 반복되는 코드 시작#######################
            if menu_s=="7": #회원탈퇴를 선택한 경우
                a.remove_member() #회원 탈퇴 또는 취소
            elif menu_s=="8": #로그아웃을 선택한 경우
                print("")
                print("<로 그 아 웃>")
                print("-"*120)
            print_login_menu()
            while select not in ["1","2","3"]:
                select=input("다시 입력해주세요(1~3): ")
                print("-"*120)
            while select=="2":
                a.create_member()
                print_login_menu()
                while select not in ["1","2","3"]:
                    select=input("다시 입력해주세요(1~3): ")
                    print("-"*120)
            if select=="1":
                while len(id_list)==0: #회원이 없는 경우에 다시 로그인 메뉴로 돌아가기 위한 코드
                    a.login() #로그인을 먼저 시도함(시도하게 되면 실패 메세지가 출력됨)
                    print_login_menu() #다시 로그인 메뉴로 돌아옴
                    while select not in ["1","2","3"]: #이 경우에도 메뉴를 잘못 선택했을 때(1, 2, 3이 아닌 다른 값을 입력했을 때)다시 선택하게 하기
                        select=input("다시 입력해주세요(1~3): ")
                        print("-"*120)
                    while select=="2": #회원가입을 선택한 경우
                        a.create_member() #회원가입 메뉴
                        print_login_menu() #회원가입 후 다시 로그인 메뉴로 돌아옴
                    if select=="3": #프로그램 종료를 선택한 경우
                        any=1 #임의로 any라는 값을 지정
                    if any==1: break
                login_again=1
                while len(id_list)!=0 and login_again==1:
                    a.login()
                    if login_again==0: break
                    print_login_menu()
                    while select not in ["1","2","3"]:
                        select=input("다시 입력해주세요(1~3): ")
                        print("-"*120)
                    while select=="2":
                        a.create_member()
                        print_login_menu()
                    if select=="3":
                        any=1
                    if any==1: break
                if any==1:
                    print("")
                    print("<프 로 그 램 종 료>")
                    print("-"*120)
                elif login_again==0:
                    a.show_timeline()
                    print("<메 인 메 뉴>")
                    print("")
                    menu=["1. 본인 회원 정보 수정","2. 타임라인글 작성 및 게시","3. 타임라인글 삭제",
                          "4. 다른 회원의 타임라인글에 좋아요","5. 타임라인글에 댓글","6. 다른 회원 정보 열람",
                          "7. 회원탈퇴","8. 로그아웃","9. 프로그램 종료"]
                    for i in menu:
                        print(i)
                        print("")
                    menu_s=input("메 뉴 선 택(숫자): ")
                    print("-"*120)
                    while menu_s not in ["1","2","3","4","5","6","7","8","9"]:
                        print("")
                        menu_s=input("다시 입력해주세요(1~9): ")
                        print("-"*120)
                    while menu_s not in ["7","8","9"]:
                        if menu_s=="1":
                            a.update_member_info()
                        elif menu_s=="2":
                            a.input_timeline()
                        elif menu_s=="3":
                            a.remove_timeline()
                        elif menu_s=="4":
                            a.add_good_response()
                        elif menu_s=="5":
                            a.input_chat()
                        elif menu_s=="6":
                            a.show_member_info()
                        a.show_timeline()
                        print("<메 인 메 뉴>")
                        print("")
                        for i in menu:
                            print(i)
                            print("")
                        menu_s=input("메 뉴 선 택(숫자): ")
                        print("-"*120)
            elif select=="3":
                print("")
                print("<프 로 그 램 종 료>")
                print("-"*120)
                break
            #####################회원탈퇴 또는 로그아웃 이후 반복되는 코드 종료######################
        if menu_s=="9": #메인 메뉴에서 프로그램 종료
            print("")
            print("<프 로 그 램 종 료>")
            print("-"*120) #
elif select=="3": #처음 로그인 메뉴에서 프로그램 종료
    print("")
    print("<프 로 그 램 종 료>")
    print("-"*120)
#######################프로그램 종료#############################
