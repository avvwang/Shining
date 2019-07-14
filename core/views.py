# --* coding:utf-8 --*
from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect, JsonResponse


# Create your views here.
def index(request):
    return render(request, "pages/index.html")


def video(request):
    return render(request, "pages/video.html")


def layer(request):
    return render(request, "layer.html")


from core.models import Case_version, Case_subversion, Case_run, Test_case

def Case(request):
    print(request.body)
    if request.method=="POST":
        return JsonResponse({"code":200})
    get_version = request.POST.get("version", "1")
    select_change = request.GET.get("select_change")
    result = Case_version.objects.get(version=10800)
    print(result.sub_version.values("id", 'Case_group', 'Case_name', "Case_list"))
    case = Case_subversion.objects.filter(id=5).values('Case_list')[0]
    executed = list(
        Case_run.objects.filter(version_id=5, result=case.get('Case_list')).values_list('Case', flat=True).distinct())
    print("已合格的用例", executed)
    print(Test_case.objects.filter(id__in=executed).values())
    print("-" * 100)
    print(get_version)
    version = Case_version.objects.values()
    print("*"*100)
    tree=[]
    for i in version.values('id',"file_name"):
        i["title"] = i.pop("file_name")
        module=list(Case_version.objects.get(id=i.get("id")).sub_version.values_list('Case_group',flat=True).distinct())
        children=[]
        for num in module:
            children.append({"title":num,"children":eval(str(list(Case_subversion.objects.filter(Case_sub_id=i.get("id"),Case_group=num).values('id','Case_name'))).replace("Case_name","title"))})
        i["children"] = children
        tree.append(i)
    print(tree)

    subversion = Case_version.objects.get(id=get_version)
    if subversion.sub_version.count() <= 1:
        return render(request, "layer.html",context={"version": version,"context":""})

    print(result.file_name, list(result.sub_version.values()))
    return render(request, "layer.html", context={"version": version, "context": list(subversion.sub_version.values()),"tree":tree})
