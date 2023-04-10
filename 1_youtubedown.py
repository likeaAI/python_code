from pytube import YouTube
from moviepy.editor import *
from pytube import Playlist

#



# 다운로드 받을 유튜브 영상 URL을 입력합니다.

download_address = input('유튜브 주소를 입력하세요\n 주소입력 : ')
yt = YouTube(download_address)

print('다운받을 거임? ')
#try :
down_answer = int(input('숫자로만 1.ok , 2.playlist로 다운_ mp3전용  \n 숫자만 입력 :'))


if down_answer == 1 :
    # 영상의 가장 높은 화질을 선택합니다. # codeck = v9
    video_tag = yt.streams.filter(res="2160p",progressive=False, video_codec="vp9").last()

    print(video_tag)
    audio = yt.streams.get_audio_only()
    print(audio)

    print('다운완료')
    print("제목 : ", yt.title)
    print("길이 : ", yt.length)
    print("게시자 : ", yt.author)
    print("게시날짜 : ", yt.publish_date)
    print("조회수 : ", yt.views)
    print("키워드 : ", yt.keywords)
    print("설명 : ", yt.description)
    print("썸네일 : ", yt.thumbnail_url)

    # 다운로드합니다.
    video = yt.streams.get_by_itag(315)

    video.download('/Users/book/Downloads/' , filename=yt.title + '.mp4')
    audio.download('/Users/book/Downloads/' , filename=yt.title + '.mp3')

    # 4k 오디오 비디오 인코딩

    # 비디오 파일 불러오기
    # 비디오 파일 불러오기

    clip = VideoFileClip('/Users/book/Downloads/' + yt.title + '.mp4')

    # 오디오 파일 불러오기
    audio = AudioFileClip('/Users/book/Downloads/' + yt.title + '.mp3')

    # 오디오 파일 추가하기
    clip = clip.set_audio(audio)

    # 비디오 파일 저장하기
    clip.write_videofile("incoding" + yt.title + '.mp4')


if down_answer == 2 :

    playlist_link = download_address
    # 플레이리스트 생성
    playlist = Playlist(playlist_link)

    # 플레이리스트에서 동영상 다운로드
    for video in playlist.videos:
        video.streams.get_highest_resolution().download()

else :
    print('다시해봐 ')


