


# 이 파일에 게임 스크립트를 입력합니다.

# image 문을 사용해 이미지를 정의합니다.
# image eileen happy = "eileen_happy.png"

## 메인 메뉴(홈 화면)에서 재생될 배경음악입니다.
define config.main_menu_music = "audio/main_title_bgm.wav"
## 사운드
define fireworks = "audio/fireworks.mp3"
define playful_bgm = "audio/playful_bgm.mp3"
define festival_bgm = "audio/festival_bgm.wav"
define romance_bgm = "audio/romance_bgm.flac"

# 게임에서 사용할 캐릭터를 정의합니다.

# script.rpy 파일 상단에 작성
define sana = Character("사나", color="#ffffff")
define haru = Character("하루", color="#ffffff")          

define narrator = Character(None)
define config.name = _("여름빛이 너에게 물들 때")

# 이미지 정의
image bg library_day = "backgrounds/bg library_day.jpg"
image bg library_twilight = "backgrounds/bg library_twilight.jpg"
image bg festival_evening = "backgrounds/bg festival_evening.jpg"
image bg hill_night = "backgrounds/bg hill_night.jpg"
image bg hill_fireworks = "backgrounds/bg hill_fireworks.jpg"
image fireworks = "backgrounds/fireworks.png"
image bg library_can = "backgrounds/bg library_can.png"

image haru normal = "characters/haru_normal.png"
image haru sigh = "characters/haru_sigh.png"
image haru annoyed = "characters/haru_annoyed.png"
image haru surprised = "characters/haru_surprised.png"
image haru blush = "characters/haru_blush.png"
image haru smile = "characters/haru_smile.png"
image haru embarrassed = "characters/haru_embarrassed.png"

image haru plain embarrassed = "characters/haru_plain_embarrassed.png"
image haru plain surprised = "characters/haru_plain_surprised.png"
image haru plain blush = "characters/haru_plain_blush.png"
image haru plain smile = "characters/haru_plain_smile.png"
image haru plain normal = "characters/haru_plain_normal"

image sana smile  = "characters/sana_smile.png"
image sana blush  = "characters/sana_blush.png"
image sana surprised  = "characters/sana_surprised.png"

image sana festival surprised  = "characters/sana_festival_surprised.png"
image sana festival blush  = "characters/sana_festival_blush.png"
image sana festival smile  = "characters/sana_festival_smile.png"
image sana festival  = "characters/sana_festival.png"
image sana festival sad  = "characters/sana_festival_sad.png"

screen choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption:
                action i.action 
                # 선택지 버튼을 클릭했을 때 소리
                activate_sound "audio/button_click.mp3"



# 폰트

#인게임 글자
define gui.text_font = "NanumBarunGothic.ttf"
#캐릭터 이름
define gui.name_font = "NanumBarunGothic.ttf"
#인터페이스
define gui.interface_text_font = "NanumBarunGothic.ttf"


# 여기에서부터 게임이 시작합니다.

# script.rpy
# 《여름빛이 너에게 물들 때》
# 플레이 타임: 약 10~20분 (목표)
# 엔딩: TRUE / NORMAL / BAD

# ==============================================================================
# 1. 캐릭터 및 변수 정의 (Define Characters & Variables)
# ==============================================================================


# 호감도 변수
default sana_favor = 0

# 스크립트 맨 위에 추가
define flash = Fade(0.1, 0.0, 0.5, color="#ffffff")


# ==============================================================================
# 2. 게임 시작 (Game Start)
# ==============================================================================

label start:

    # --------------------------------------------------------------------------
    # [Scene 1: 일상 - 여름날 오후의 도서관]
    # --------------------------------------------------------------------------
    play music "audio/playful_bgm.mp3" fadein 1.0
    scene bg library_day
    with fade

    "창밖에서는 매미 소리가 지칠 줄 모르고 울려 퍼지고 있었다."
    "에어컨 바람이 선선하게 불어오는 여름 방학 일주일 전의 도서관."
    "이곳은 내가 가장 좋아하는 공간이자..."

    # 하루와 사나 함께 등장 (왼쪽: 하루 / 오른쪽: 사나)
    show haru normal at left
    show sana smile at right
    with dissolve

    "내가 가장 좋아하는 사람이 있는 공간이다."

    show haru sigh
    "나는 책을 정리하며 혼잣말을 중얼거렸다"
    haru "...학생회장은 참 부지런하네. 방학 전이라고 업무가 그렇게 많은가."

    sana "아, 진짜~! 하루! 혼잣말하는 척하면서 나 들으라고 디스하는 거지?"

    show haru surprised
    haru "앗... 들렸어?"

    sana "다 들리거든? 학생회 일이 얼마나 많은지 네가 알아? 도서부원이라고 맨날 에어컨 밑에서 책만 읽는 하루는 모를 거야!"

    "투덜거리면서도 사나는 내 옆자리 의자를 소리 없이 스르륵 끌어당겨 앉았다."
    "금발 머리칼이 바람에 날리며 향긋한 샴푸 향이 내 코끝을 스쳤다. 나도 모르게 가슴이 쿵쾅거리기 시작한다."

    show haru normal
    haru "그렇게 불만이면 좀 쉬다 가든가. 아무도 뭐라 안 해, 회장님."

    sana "히히, 그럴 줄 알고 이미 땡땡이치는 중이지! 여기, 네가 좋아하는 이온 음료 사 왔어."

    scene library_can

    "사나가 주머니에서 차가운 음료캔을 꺼내 내 뺨에 슬쩍 가져다 대었다."

    
    haru "아, 차가워! 진짜, 깜짝 놀랐잖아..."

    sana "으하하! 반응 진짜 솔직하다니까, 하루는. 자, 받아!"


    # --------------------------------------------------------------------------
    # [Scene 2: 티격태격 & 첫 번째 선택지 구간]
    # --------------------------------------------------------------------------

    "캔을 받아들며 손끝이 살짝 닿았다. 사나는 아무렇지도 않은 듯 웃고 있지만, 나는 얼굴이 화끈거리는 것을 숨기려 고개를 돌렸다."

    scene bg library_day
    show haru normal at left
    show sana_smile at right

    sana "근데 하루야, 방학하면 도서관 매일 안 나올 거잖아. 나 심심해서 어쩌지?"

    haru "뭐... 집에서 책 읽거나 공부하겠지. 너는 친구 많으니까 다른 애들이랑 놀면 되잖아."

    sana "에이, 다들 방학이라고 여행 가고 학원 가느라 바쁘단 말이야."

    show haru normal at left
    show sana_blush at right
    sana "그리고... 나는 하루랑 있는 게 제일 편한데."

    "툭 던져진 뜻밖의 진심. 사나는 정말 아무 의도 없이 한 말일까?"
    "쿵쾅거리는 심장을 누르며, 어떤 말을 할지 망설여졌다."

    # --- 선택지 1 ---
    menu:
        "나도 사나랑 있는 게 제일 좋아.":
            $ sana_favor += 1
            
            show haru blush
            haru "나, 나도... 너랑 있을 때가 제일 좋은데."

            show sana_blush at right
            sana "어...? 그, 그래? 그렇게 솔직하게 말하면 내가 놀라잖아..."

            "사나가 예상을 못 했다는 듯 둥그렇게 눈을 뜨더니, 이내 귓가가 붉어진 채 고개를 돌렸다."

        "나한테 치근덕거리지 말고 공부나 해.":
            show haru annoyed
            haru "나한테 치근덕거릴 시간에 학생회 일이나 빨리 끝내시죠, 회장님."

            sana "뭐야~! 매정한 것 봐! 사람이 진심을 담아서 말했더니!"

            "사나가 삐친 척 볼을 빵빵하게 부풀렸지만, 나를 바라보는 눈빛에는 장난기가 가득했다."
            sana "하여간 쑥스러우면 꼭 저렇게 차갑게 굴더라~ 다 티 나거든?"

        "방학 때도 도서관 나올 건데? 너 보러.":
            $ sana_favor += 2

            show haru blush
            haru "방학 때도 매일 도서관 나올 생각인데. 너 오면 만나려고."

            show sana surprised at right
            sana "지, 진짜?! 나 보려고 나오는 거야?!"

            "사나가 너무 놀란 나머지 의자를 바짝 당겨 다가왔다. 얼떨결에 우리 둘의 거리가 한 뼘도 채 되지 않게 가까워졌다."
            sana "잠깐만, 하루야... 방금 건 좀 가깝잖아..."


    # --------------------------------------------------------------------------
    # [Scene 3: 심쿵 포인트 & 불꽃놀이 축제 제안]
    # --------------------------------------------------------------------------
    show haru normal
    show sana smile at right
    with dissolve

    haru "그나저나 여름 방학 계획은 다 세웠어? 회장 일 때문에 바빠서 아무것도 못 정했을 것 같은데."

    sana "응... 사실 맞아. 하고 싶은 건 많은데 막상 혼자 가기는 좀 그렇고..."

    "사나가 손가락을 조물거리며 내 눈치를 슬금슬금 살폈다. 평소의 당당한 학생회장 모습과는 전혀 다른 모습이었다."

    sana "있잖아, 하루야. 혹시... 방학 시작하는 날에 시간 있어?"

    haru "방학식 날? 딱히 특별한 일은 없는데."

    "사나가 갑자기 숨을 들이쉬더니, 내 손목을 꼭 쥐었다. 손끝에서 전달되는 사나의 체온에 가슴이 터질 것처럼 뛰기 시작했다."

    show sana blush
    sana "그럼... 나랑 같이 축제 가지 않을래? 방학식 날 저녁에 근처 신사에서 불꽃놀이 축제 하잖아!"

    show haru surprised
    haru "불꽃놀이...? 단둘이?"

    sana "으, 응! 단둘이! 다른 애들한테는 비밀로 하고... 둘이서만 가고 싶어서..."


    # --------------------------------------------------------------------------
    # [Scene 4: 승낙 여부 - 두 번째 선택지 구간]
    # --------------------------------------------------------------------------
    "사나의 얼굴이 노을빛 때문인지, 아니면 수줍음 때문인지 붉게 물들어 있었다."
    "언제나 빛나고 멀게만 느껴졌던 학생회장이, 지금은 오직 나만을 바라보며 답을 기다리고 있다."

    # --- 선택지 2 ---
    menu:
        "좋아, 같이 가자.":
            $ sana_favor += 1
            
            show haru smile
            haru "좋아. 같이 가자, 사나야."

            show sana smile
            sana "정말?! 약속했다! 딴소리하기 없기다?!"

            "사나가 아이처럼 환하게 웃으며 내 손을 꼭 잡았다."
            sana "히히... 사실 전부터 하루랑 꼭 가보고 싶었어. 방학식이 벌써 기다려진다."

        "음... 내가 가도 재미없을 텐데?":
            show haru embarrassed
            haru "나 조용해서 너랑 가봤자 재미없을 텐데... 괜찮겠어?"

            sana "하루랑 같이 있는 거 자체가 즐겁다니까? 자꾸 이상한 소리 할래?"

            "사나가 내 손목을 잡은 손에 살며시 힘을 주었다."
            sana "하루는 조용히 내 옆에 있어 주기만 하면 돼. 그러니까... 가 주는 거지?"

            show haru smile
            haru "...응. 가자."


    # --------------------------------------------------------------------------
    # [Scene 5: 노을녘 도서관 & 다음 장을 향한 복선]
    # --------------------------------------------------------------------------
    scene bg library_twilight
    show haru normal at left
    show sana smile at right
    with fade

    "어느덧 창밖은 붉은 노을로 물들어가고 있었다."
    "도서관 정적 속에서 서로의 숨소리와 빠르게 뛰는 심장 소리만이 조용히 울려 퍼졌다."

    sana "아! 벌써 시간이 이렇게 됐네. 나 학생회실 돌아가 봐야겠다!"

    "사나가 가방을 챙기며 자리에서 일어났다. 그리고 도서관 문을 열기 전, 나를 돌아보며 상큼하게 웃어 보였다."

    sana "오늘 약속 잊으면 안 돼, 하루야! 방학식 날, 엄청 기대하고 있을 테니까!"

    hide sana with dissolve

    "문이 닫히고 다시 도서관에는 조용한 매미 소리만 남았다."
    "식지 않은 사나의 온기가 남아있는 내 손목을 가만히 감싸 잡았다."

    show haru blush
    haru "(...큰일이다. 방학까지 일주일이나 남았는데, 벌써 잠이 안 올 것 같아.)"

    jump festival_preparation


# ==============================================================================
# 4. 중반부: 방학식 날 저녁, 불꽃놀이 축제 데이트
# ==============================================================================

label festival_preparation:

    # --------------------------------------------------------------------------
    # [Scene 6: 일주일 뒤 - 축제장 근처 신사 입구]
    # --------------------------------------------------------------------------
    scene bg festival_evening
    with fade
    play music "audio/festival_bgm.wav" fadein 1.0

    "일주일이라는 시간이 어떻게 지났는지 모르겠다."
    "드디어 찾아온 방학식 날 저녁. 붉게 노을이 지는 신사 입구는 벌써 사람들로 북적였다."

    show haru plain embarrassed at left
    with dissolve
    
    "나는 안절부절못하며 사나를 기다렸다."
    haru "너무 일찍 왔나... 30분이나 먼저 도착해 버렸네."

    "평소 입던 교복이 아닌 사복 차림이라 괜히 어색해서 옷자락만 만지작거렸다."
    "그때, 저 멀리서 다가오는 익숙한 금발 머리가 눈에 들어왔다."

    show sana festival at right
    with dissolve

    "사나는 평소와 다른 유카타 차림에 머리까지 예쁘게 땋아 올린 모습이었다."
    "화려하고 반짝이는 사나의 모습에 나도 모르게 숨을 헉 하고 들이쉬었다."

    show haru plain surprised
    haru "사, 사나야...!"

    sana "하루야~! 많이 기다렸어? 어때, 나 잘 어울려?"

    "사나가 내 앞에서 빙르르 한 바퀴 돌며 웃어 보였다. 순간 사나에게서 눈을 뗄 수가 없었다."

    # --- 선택지 3: 사나의 유카타 차림에 대한 반응 ---
    menu:
        "너무 예뻐서 순간 못 알아봤어.":
            $ sana_favor += 2

            show haru plain blush
            haru "너무 예뻐서... 순간 다른 사람인 줄 알고 못 알아볼 뻔했어."

            show sana festival blush
            sana "뭐, 뭐야~ 싱겁기는! 귀여운 소리 하고 있네..."

            "사나가 수줍은 듯 볼을 붉히며 시선을 살짝 피했다."

        "응, 평소보다 훨씬 잘 어울려.":
            $ sana_favor += 1

            show haru plain smile
            haru "응, 진짜 잘 어울린다. 평소 모습도 좋지만 오늘은 더 특별해 보여."

            sana "히히, 다행이다! 하루한테 잘 보이려고 엄청 신경 써서 입고 나왔거든!"

        "(부채질을 해주며) 덥진 않아?":
            show haru plain normal
            haru "예쁘긴 한데... 옷이 좀 답답해 보인다. 덥진 않아?"

            sana "에이~ 분위기 깨게 덥긴 뭐가 더워! ...사실 조금 덥긴 한데 하루가 있으니까 괜찮아!"


    # --------------------------------------------------------------------------
    # [Scene 7: 축제 거리 탐방 & 소소한 스킨십]
    # --------------------------------------------------------------------------
    "우리는 야시장 포장마차 거리를 걸으며 타코야끼와 사과 사탕을 사 먹었다."
    "축제의 시끌벅적함 속에서, 사나와 함께 걷는 이 시간 자체가 꿈만 같았다."

    show haru plain normal
    show sana festival smile
    with dissolve

    sana "아! 하루야, 저기 사격 게임 있다! 나 저기 있는 곰 인형 갖고 싶어!"

    haru "곰 인형? 어디 볼까... 음, 사격은 나 약간 자신 있는데."

    sana "진짜?! 그럼 하루가 나 대신 인형 따주면 안 돼? 제발~!"

    "반짝이는 눈으로 나를 바라보는 사나의 청을 거절할 수 있을 리가 없다."

    # --- 선택지 4: 미니 게임 도전 ---
    menu:
        "(신중하게 장전을 하며) 인형을 노린다.":
            $ sana_favor += 1

            "나는 숨을 고르고 정확히 곰 인형의 받침대를 향해 총을 쏘았다."
            "탕-!"
            "경쾌한 소리와 함께 곰 인형이 톡 떨어졌다."

            show haru plain smile
            haru "자, 여기. 네 선물이야."

            show sana festival smile
            sana "와아! 대박! 하루 진짜 멋있다! 최고야!"

            "사나가 감격했는지 인형을 끌어안으며 내 팔을 꼬옥 안아왔다."

        "(장난스럽게) 사나 손을 잡고 같이 쏜다.":
            $ sana_favor += 2

            show haru plain blush
            haru "혼자 쏘는 것보다 같이 하는 게 재밌잖아. 자, 손 이렇게 잡고..."

            "나는 사나의 뒤로 다가가 사나의 손을 감싸 쥐었다."

            show sana festival blush
            sana "앗... 하루야, 갑자기 이렇게 가까우면..."

            "탕-!"
            "사나가 당황해서 얼떨결에 방아쇠를 당겼지만, 다행히 표적에 맞아 인형이 떨어졌다."

            sana "정말... 미리 말을 해주고 들어오든가 하지..."


    # --------------------------------------------------------------------------
    # [Scene 8: 인파 속에서 조용한 언덕으로]
    # --------------------------------------------------------------------------
    "어느덧 불꽃놀이가 시작될 시간이 다가오자 축제장에 사람들이 몰려들기 시작했다."
    "사람 밀물에 밀려 사나와 거리가 벌어지려던 순간-"

    sana "앗, 하루야...!"

    "사나가 내 옷자락을 꽉 쥐었다. 사람들에게 휩쓸릴까 봐 불안해하는 기색이 역력했다."

    show haru plain normal
    haru "여기는 사람이 너무 많네. 사나야, 손잡자. 놓치면 안 되니까."

    "나는 망설임 없이 사나의 작은 손을 꼭 잡았다."
    "우리는 북적이는 사람들을 피해 신사 뒤편의 조용한 언덕길로 걸어 올라갔다."


    # --------------------------------------------------------------------------
    # [Scene 9: 감정의 절정 - 불꽃놀이와 고백의 전조]
    # --------------------------------------------------------------------------
    scene bg hill_night
    show haru plain normal at left
    show sana festival smile at right
    with fade
    play music "audio/romance_bgm.flac" fadein 1.0

    "언덕 위에 오르자 축제장의 소음이 아득하게 들리고, 시원한 밤바람이 불어왔다."
    "아래로는 축제장의 불빛이, 위로는 밤하늘이 넓게 펼쳐져 있었다."

    haru "여기라면 불꽃이 잘 보이겠다. 사람도 없고 조용하네."

    sana "응... 하루랑 둘만 있는 것 같아."

    "사나는 잡고 있던 내 손을 놓지 않은 채 하늘을 올려다보았다."

    # 펑-! 펑-! (불꽃놀이 효과음 및 연출)
    play sound "audio/fireworks.mp3"
    scene bg hill_fireworks
    show haru plain surprised at left
    show sana festival smile at right
    with flash

    "퍼펑-!"
    "화려한 불꽃이 밤하늘을 수놓으며 사나의 얼굴을 붉고 푸르게 물들였다."
    "아름다운 불꽃놀이였지만, 내 눈은 자꾸만 옆에 있는 사나에게로 향했다."

    show haru plain blush
    haru "...불꽃보다 훨씬 예쁘다."

    sana "응? 하루야, 뭐라고 했어?"

    haru "아, 아니! 아무것도 아니야!"

    "사나가 피식 웃더니 내 쪽으로 한 걸음 더 다가왔다. 둘 사이의 거리가 숨소리가 들릴 만큼 가까워졌다."

    show sana festival blush
    sana "하루야. 사실 나... 오늘 너한테 꼭 하고 싶었던 말이 있어."

    haru "하고 싶었던 말...?"

    sana "응. 일주일 동안 도서관에서 너랑 대화하면서... 방학이 오는 게 너무 싫었어."
    sana "방학하면 매일 너를 못 보게 되니까..."

    scene fireworks

    "사나의 진지한 눈빛이 나를 직시했다. 심장이 터질 것처럼 쿵쾅거리기 시작했다."

    sana "나한테 있어서 하루는... 그냥 편한 친구 이상이야."
    sana "너는... 나를 어떻게 생각해?"

    # 분기점으로 연결
    jump climax_confession


# ==============================================================================
# 5. 후반부: 고백 및 엔딩 (Climax & Ending)
# ==============================================================================

label climax_confession:

    # --------------------------------------------------------------------------
    # [Scene 10: 마음을 전하는 순간]
    # --------------------------------------------------------------------------
    "밤하늘에서는 화려한 불꽃이 쉴 새 없이 터지고 있었지만, 세상의 모든 소리가 멀어지는 듯했다."
    "사나의 오롯한 눈동자에 노을빛보다 더 붉어진 내 얼굴이 비쳤다."

    "항상 빛나고 완벽해 보이던 학생회장 사나가, 지금 내 답을 기다리며 떨리는 손으로 내 손가락을 꼭 쥐고 있다."

    # --- 최종 고백 선택지 ---
    menu:
        "나도 사나 너를 좋아해. 아주 오래전부터.":
            $ sana_favor += 2

            haru "나도... 나도 너를 좋아해, 사나야."
            haru "그냥 친구로 생각한 적 단 한 번도 없어. 도서관에서 너와 함께 보낸 모든 순간이 내겐 전부 특별했어."
            
            sana "하루야... 정말...?"
            
            haru "응. 축제에 같이 가자고 해줘서 정말 기뻤어. 사나 너만 괜찮다면... 앞으로도 계속 네 옆에 있고 싶어."

            "말을 마치는 순간, 사나의 눈가에 눈물이 살짝 고이더니 이내 꽃이 피듯 환한 미소가 번졌다."
            
            sana "우으... 정말이지, 말은 그렇게 솔직하게 하면서 왜 지금까지 숨긴 거야..."

        "너처럼 빛나는 애가 나 같은 걸 좋아해 줄 줄은 몰랐어.":
            $ sana_favor += 1

            scene bg hill_fireworks
            show haru plain embarrassed at left
            haru "너는 언제나 인기 많고 빛나는 사람이니까... 나 같은 애가 좋아해도 되는지 많이 망설였어."
            haru "하지만 사나야, 나도 너를 정말 좋아해."

            show sana festival smile at right
            sana "바보... 빛난다니 무슨 소리야. 너랑 같이 있을 때의 내가 가장 나다운 모습인데."

            "사나가 수줍게 웃으며 잡고 있던 내 손에 온기를 더했다."

        "너무 갑작스러워서... 아직은 마음을 잘 모르겠어.":
            
            scene bg hill_night
            show haru plain embarrassed
            haru "미안해, 사나야... 네 마음은 정말 고맙지만, 너무 갑작스러워서 당장은 확실히 말을 못 하겠어..."

            hide haru
            show sana festival sad
            sana "아... 그렇구나. 미안해, 내가 너무 급했지?"

            "사나는 씁쓸한 미소를 지었지만, 이내 마음을 다잡듯 내 손을 살며시 놓아주었다."
            sana "괜찮아! 당장 답을 들으려고 한 건 아니니까. 방학 동안 천천히 생각해 줘."
            jump normal_ending


    # --------------------------------------------------------------------------
    # [Scene 11: 엔딩 분기 (호감도 조건 판정)]
    # --------------------------------------------------------------------------
    # 누적 호감도가 4점 이상이면 HAPPY END, 미만이면 NORMAL END로 이동
    if sana_favor >= 4:
        jump happy_ending
    else:
        jump normal_ending


# ==============================================================================
# 6-A. HAPPY END: 가장 특별한 여름 방학의 시작
# ==============================================================================

label happy_ending:

    scene bg hill_fireworks
    show haru plain blush at left
    show sana festival blush at right
    with dissolve

    "사나가 까치발을 들더니 내 볼에 살며시 입을 맞추었다."
    "쪽 하는 간지러운 감촉과 함께 얼굴이 터질 듯이 뜨거워졌다."

    show haru plain surprised
    haru "사, 사나야...?!"

    show sana festival smile
    sana "히히, 이건 내 마음의 도장! 이제 딴소리하기 없기다?"

    "불꽃놀이의 마지막 거대한 불꽃이 밤하늘을 화려하게 수놓았다."
    "사나는 내 손가락 사이로 자신의 손가락을 겹쳐 잡으며 깍지를 꼈다."

    sana "하루야, 남은 여름 방학 동안 하고 싶은 게 너무 많아."
    sana "바다도 가고, 영화도 보고, 도서관에서 둘이서만 데이트도 하고..."

    show haru plain smile
    haru "응, 다 가자. 네가 가고 싶은 곳이라면 어디든 같이 갈게."

    sana "약속했다? 내 첫 번째 여자친구님!"

    "시원한 밤바람 속에서 우리 둘의 잡은 손은 밤이 새도록 식지 않았다."
    "짝사랑으로 끝날 줄 알았던 나의 여름은, 그 어느 때보다 달콤하고 특별하게 시작되고 있었다."

    # 연애 성공 엔딩 연출
    hide haru
    hide sana
    with dissolve
    
    scene black with fade
    centered "{color=#f39c12}{b}HAPPY END : 여름날의 불꽃, 그리고 너와 나{/b}{/color}"
    
    return


# ==============================================================================
# 6-B. NORMAL END: 여운이 남는 여름의 계절
# ==============================================================================

label normal_ending:

    scene bg hill_night
    show haru plain normal at left
    show sana festival smile at right
    with dissolve

    "축제의 마지막 불꽃이 올려다본 밤하늘 속으로 스러져 갔다."
    "약간의 어색함과 수줍음이 우리 사이에 맴돌았지만, 그 분위기조차 싫지 않았다."

    sana "푸훗... 우리 방학식 날부터 너무 거창하게 보낸 거 아니야?"

    show haru plain smile
    haru "그러게. 항상 도서관에만 있다가 이렇게 나오니까 색다르긴 하네."

    "사나는 가볍게 기지개를 켜며 나를 향해 돌아섰다."

    sana "솔직히 말해줘서 고마워, 하루야. 덕분에 오늘 축제 너무 즐거웠어."

    haru "나도. 내 인생에서 가장 기억에 남는 축제가 될 것 같아."

    "언덕을 내려가는 길, 이전처럼 격의 없이 티격태격 대화가 이어졌지만..."
    "서로를 바라보는 눈빛 속에는 분명 이전과는 다른 작은 설렘이 자리 잡고 있었다."

    show haru plain blush

    haru "...우리의 여름은 이제 막 시작되었을 뿐이야."

    # 여운을 남기는 열린 엔딩 연출
    hide haru
    hide sana
    with dissolve

    scene black with fade
    centered "{color=#8c6d58}{b}NORMAL END : 푸른 계절의 서막{/b}{/color}"

    return