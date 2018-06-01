import os
import subprocess
import shutil
import pytube


def download(link, num):
    yt = pytube.YouTube(link)  # 다운받을 동영상 URL 지정
    vids = yt.streams.all()

    # 영상 형식 리스트 확인
    # for i in range(len(vids)):
    #    print(i, '. ', vids[i])

    # 저장 경로 지정(Windows or mac)
    parent_dir = "C:\\Users\\kwon\\Desktop\\개인 프로젝트\\화자인식을 위한 CNN 기반 음성인식 알고리즘의 개발\\데이터\\" + num

    if os.path.exists(parent_dir):  # 이미 존재하는 경우, 삭제를 할까..
        try:
            shutil.rmtree(parent_dir)
        except OSError as e:
            if e.errno == 2:
                print  # 파일이나 디렉토리가 없음!
                'No such file or directory to remove'
                pass
            else:
                raise

    # 디렉터리 생성
    os.mkdir(parent_dir)

    vnum = 1

    # 다운로드 수행
    vids[vnum].download(parent_dir)

    # 파일 변환
    new_filename = num + '.wav'
    default_filename = vids[vnum].default_filename

    # cmd 명령어 수행
    subprocess.call(
        ['ffmpeg', '-i', os.path.join(parent_dir, default_filename), os.path.join(parent_dir, new_filename)])

    print(num + '번 동영상 다운로드 및 mp3 변환 완료!')


f = open("C:\\Users\\kwon\\Desktop\\개인 프로젝트\\화자인식을 위한 CNN 기반 음성인식 알고리즘의 개발\\데이터\\download.txt")
links = f.readlines()
f.close()

for i in range(len(links)):
    print(links[i])
    download(links[i], str(i + 1))



