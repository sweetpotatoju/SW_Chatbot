from django.shortcuts import render, redirect

# Create your views here.

# 비밀번호 페이지
def admin_page(request):

    if request.method == "POST":
        password = request.POST.get('password')
        if password == '1234':  # 관리자 비밀번호
            # 비밀번호가 일치하면 메인 페이지로 리디렉션

            return redirect('management')
        else:
            # 비밀번호가 틀렸을 때 별도의 응답 없이 아무 것도 하지 않음
            return render(request, 'chatbotAdmin/admin_page.html')

    return render(request, 'chatbotAdmin/admin_page.html')

# 비밀번호 해제 후, 메인 화면
def management(request):
    return render(request, 'chatbotAdmin/management.html')

# 공지 추가 페이지
def add_notice(request):
    if request.method == "POST":
        # DB 연결 필요(버튼 선택 시 아무 행동 x)
        return render(request, 'chatbotAdmin/add_notice.html')
    return render(request, 'chatbotAdmin/add_notice.html')
