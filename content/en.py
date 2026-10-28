"""English, the site's default language, served at the root."""

CODE = "en"
HTML_LANG = "en"
HREFLANG = "en"
OG_LOCALE = "en_US"
PLAY_HL = None
LABEL = "English"
PREFIX = ""
BRAND = "Classic Board Games"
BADGE = "google-play-badge.png"
# Animal Chess diagrams show each piece's rank (1-8) unless a language gives one-character names.
ANIMAL_NAMES = None

UI = dict(
    nav_games="Games", nav_shots="Screenshots", nav_faq="FAQ", language="Language",
    badge_alt="Get it on Google Play",
    privacy="Privacy policy",
    trademark="Google Play and the Google Play logo are trademarks of Google LLC.",
    crumbs_games="Games",
    vs="vs AI or a friend", offline="Works offline", free="Free",
    how_to_play="How to play {name}",
    in_app="{name} in Classic Board Games Offline",
    eleven_more="Eleven more classic board games in the same free app, all playable offline.",
    phone_alt="{name} in Classic Board Games Offline on Android",
    more_games="More games in the app",
    cta_game="Play {name} for free",
    cta_game_lead="On Android phones and tablets, with no internet needed.",
    detail_link="Full rules with diagrams",
    shot_alt="{caption} in Classic Board Games Offline",
)

INDEX = dict(
    title="Classic Board Games Offline – Animal Chess, Chess, Xiangqi, Shogi & more",
    desc=("12 classic board games in one free Android app: Animal Chess (Dou Shou Qi), Chess, Xiangqi, Shogi, "
          "Gomoku, Luzhanqi, Yutnori, Ludo and more. Play offline against the AI or a friend."),
    app_desc="Twelve classic board games in one app, played offline against the AI or a friend.",
    eyebrow="Free board games for Android",
    h1="Classic Board Games Offline",
    lead=("Twelve board games from East and West in one small app: Animal Chess (Dou Shou Qi), Chess, "
          "Xiangqi, Shogi, Gomoku, Luzhanqi, Yutnori, Ludo and more. Play the AI or a friend on one device, with no "
          "internet and no sign-in."),
    facts=["12 games", "Works offline", "3 AI levels", "2–6 players on one device", "10 languages"],
    hero_alt="The Classic Board Games lobby with all twelve games",
    games_h2="Twelve games, one app",
    games_lead=("Every game has its real rules, a computer opponent with three levels, and a two-player mode for "
                "playing face to face on one phone or tablet. Pick one to read the rules."),
    asian_h2="The Asian board games you grew up with",
    asian=["Most board game apps stop at Chess and Ludo. This one also brings the games played on kitchen tables, "
           "school desks and New Year floors across Asia: Chinese Chess and Japanese Shogi, Gomoku, the Animal Chess "
           "every child in China knows, the bluffing battles of Army Chess, the Flying Chess race, and Korea's Yutnori.",
           "They are hard to find in one place, and harder to find with an opponent who knows the rules. Here each one "
           "has a computer player that does, and it plays without an internet connection."],
    chips=[("animal-chess", "斗兽棋"), ("xiangqi", "象棋"), ("shogi", "将棋"), ("gomoku", "五子棋"),
           ("luzhanqi", "军棋"), ("aeroplane-chess", "飞行棋"), ("yutnori", "윷놀이")],
    asian_alt="Animal Chess (Dou Shou Qi) on a tablet",
    shots_h2="Screenshots",
    shots_lead="Wooden boards, traditional pieces and a calm green table, on phones and tablets.",
    shots=[("lobby", "Twelve games, one lobby"), ("chess", "Chess"), ("xiangqi", "Xiangqi"),
           ("animal-chess", "Animal Chess"), ("luzhanqi", "Luzhanqi deployment"), ("gomoku", "Gomoku"),
           ("ludo", "Ludo"), ("yutnori", "Yutnori"), ("shogi", "Shogi"), ("chinese-checkers", "Chinese Checkers")],
    features_h2="Built to stay out of your way",
    features=[
        ("Play the AI or a friend", "Easy, Normal and Expert AI. Two players on one device, up to four in Ludo and "
                                    "Aeroplane Chess and six in Chinese Checkers. Any seat can be a person or the AI, "
                                    "even AI against AI."),
        ("Offline, no account", "The games and the AI run on your device. No account, no sign-in, a small download "
                                "and light on battery."),
        ("Undo, replay, save", "Take back a move, replay a finished game from the start, keep a separate save for "
                               "every game, and add an optional chess clock."),
        ("No pop-up ads", "One small banner on the result screen, and rewarded ads only when you choose to watch one. "
                          "A one-time Premium purchase removes all of it."),
        ("Phone and tablet", "A real tablet layout with a side panel, not a stretched phone screen, and ten interface "
                             "languages."),
    ],
    faq_h2="Questions",
    faq=[
        ("Is it free?", "Yes. All twelve games, the Easy and Normal AI, and two-player games on one device are free and "
                        "unlimited. Optional short ads add extra Undo and Load uses, and a one-time Premium purchase "
                        "unlocks the Expert AI, unlimited Undo and Load, and removes all ads. There is no subscription."),
        ("Does it work offline?", "Yes. Every game and the AI run on your phone, so you can play on a plane, on the "
                                  "subway or anywhere without a signal. Only ads and purchases use the internet."),
        ("Can two people play on one phone?", "Yes. Every game supports pass-and-play on one device. Ludo and Aeroplane "
                                               "Chess take up to four players and Chinese Checkers up to six, and any "
                                               "seat can be a person or the AI."),
        ("Do I need an account?", "No. There is no account and no sign-in."),
        ("Which languages does it support?", "Ten: English, 简体中文, 日本語, 한국어, Tiếng Việt, Bahasa Melayu, ไทย, ລາວ, "
                                             "Español, Deutsch."),
        ("Which devices does it run on?", "Android 7.0 or newer, on phones and tablets. Tablets get their own layout "
                                          "with a side panel rather than a stretched phone screen."),
    ],
    cta_h2="Ready for a game?",
    cta_lead="Free on Google Play for Android phones and tablets.",
)

GAMES = [
    dict(slug="chess", name="Chess", aka="International chess", players="2 players",
         title="Chess Offline – Play vs AI or a Friend, Free for Android",
         desc="Play chess offline on Android against an AI with three levels, or with a friend on the same phone. Free, no account and no Wi-Fi needed.",
         intro="The world's classic strategy game: two armies of sixteen pieces and one goal, to checkmate the enemy king. Learn the moves in an afternoon, then spend years getting better.",
         rules=["Each side has a king, a queen, two rooks, two bishops, two knights and eight pawns.",
                "White moves first and the players alternate, one move each.",
                "Capture by moving onto the square of an enemy piece.",
                "Castling, en passant and pawn promotion are all part of the game.",
                "Checkmate the opposing king to win; a stalemate is a draw."],
         app=["Play the computer at Easy, Normal or Expert, or a friend on one device.",
              "The AI opens from a built-in chess opening book, then thinks for itself.",
              "Optional chess clock, undo, and a replay of the whole game."]),
    dict(slug="xiangqi", name="Xiangqi", aka="Chinese Chess · 象棋", players="2 players",
         title="Xiangqi (Chinese Chess 象棋) Offline – Free Android App",
         desc="Play Xiangqi, Chinese Chess (象棋), offline on Android against an AI with a real opening book or with a friend on one phone. Free, no sign-in.",
         intro="Chinese Chess is played on the points of a 9×10 board split by a river. Generals stay inside their palace, cannons leap to capture, and one soldier across the river can decide the game.",
         rules=["Each side has a general, two advisors, two elephants, two horses, two chariots, two cannons and five soldiers.",
                "Pieces stand on the intersections, not in the squares. Red moves first.",
                "The general and advisors never leave the palace, and elephants never cross the river.",
                "A cannon moves like a chariot but captures by jumping over exactly one piece.",
                "A horse is blocked by a piece beside it, and the two generals may never face each other on an open file.",
                "Checkmate or stalemate the enemy general to win."],
         app=["Traditional Chinese-character pieces on a wooden board.",
              "The AI plays real Xiangqi openings from a built-in opening book.",
              "Play the computer or a friend on one device, fully offline."]),
    dict(slug="shogi", name="Shogi", aka="Japanese Chess · 将棋", players="2 players",
         title="Shogi (Japanese Chess 将棋) Offline vs AI – Free Android App",
         desc="Play Shogi, Japanese Chess (将棋), offline on Android against an AI that knows its openings, or with a friend on one device. Free, no account.",
         intro="Japanese chess on a 9×9 board, where nothing you capture is lost for good: take an enemy piece and you can drop it back onto the board as your own.",
         rules=["Each side has twenty pieces: a king, a rook, a bishop, two gold and two silver generals, two knights, two lances and nine pawns.",
                "Sente moves first.",
                "Captured pieces go to your hand, and on a later turn you may drop one onto an empty square instead of moving.",
                "Most pieces may promote when they move into, within or out of the last three ranks.",
                "Checkmate the enemy king to win."],
         app=["Traditional kanji pieces.",
              "The AI plays known openings from a built-in joseki book.",
              "Play the computer or a friend on one device."]),
    dict(slug="gomoku", name="Gomoku", aka="Five in a Row · 五子棋 · 五目並べ", players="2 players",
         title="Gomoku (Five in a Row 五子棋) Offline – Free Android App",
         desc="Play Gomoku, Five in a Row (五子棋), offline on Android against the AI or a friend. Black and white stones on a 15×15 board. Free, no Wi-Fi needed.",
         intro="Black and white stones on a 15×15 board. A minute to learn and a lifetime to master: the first player to make an unbroken line of five wins.",
         rules=["Black places first, then the players take turns putting one stone on an empty intersection.",
                "Stones never move and are never captured.",
                "Five of your stones in a row, across, down or diagonally, wins the game.",
                "Block your opponent's open threes and fours before they turn into five."],
         app=["A 15×15 wooden board with classic black and white stones.",
              "Three AI levels for a quick game on a break or a real fight.",
              "Two players can share one phone."]),
    dict(slug="checkers", name="Checkers", aka="English Draughts · American Checkers", players="2 players",
         title="Checkers (English Draughts) Offline vs AI – Free Android App",
         desc="Play checkers, English draughts, offline on Android against the AI or a friend on one phone. Classic 8×8 rules, free, no account.",
         intro="The 8×8 classic of diagonal moves and jumping captures, and the race to be crowned king.",
         rules=["Each player starts with twelve pieces on the dark squares.",
                "Pieces move one square diagonally forward.",
                "Capture by jumping an adjacent enemy piece into the empty square beyond. Jumps can be chained, and capturing is compulsory.",
                "A piece that reaches the far row is crowned and may then move backwards too.",
                "Win by capturing all of your opponent's pieces or leaving them no move."],
         app=["English / American checkers rules.",
              "Choose your colour and play the AI or a friend.",
              "Undo a move or replay the game from the start."]),
    dict(slug="four-in-a-row", name="Four in a Row", aka="The drop-disc line game", players="2 players",
         title="Four in a Row Offline – Play vs AI or a Friend on Android",
         desc="Play Four in a Row offline on Android: drop discs into a 7×6 grid and connect four before the AI or your friend does. Free, no Wi-Fi needed.",
         intro="Drop coloured discs into a grid seven columns wide and six rows high, and be the first to line up four.",
         rules=["Take turns dropping a disc into any column; it falls to the lowest empty space.",
                "Four of your discs in a line, across, down or diagonally, wins.",
                "If the grid fills up with no line of four, the game is drawn."],
         app=["Play the computer at three levels or a friend on one phone.",
              "Quick games, perfect for a short break."]),
    dict(slug="chinese-checkers", name="Chinese Checkers", aka="Star Halma · 跳棋", players="2, 3, 4 or 6 players",
         title="Chinese Checkers (跳棋) Offline – 2 to 6 Players on Android",
         desc="Play Chinese Checkers (跳棋) offline on Android with 2, 3, 4 or 6 players: friends on one device, the AI, or both. Free, no account needed.",
         intro="Race your marbles across a six-pointed star. Hop over any marble, yours or an opponent's, and chain hops together to cross the board in a single turn.",
         rules=["Each player starts with ten marbles in one point of the star.",
                "On your turn, step to a neighbouring empty hole, or hop over an adjacent marble into the empty hole beyond.",
                "Hops can be chained in one turn, and nothing is ever captured.",
                "The first player to move all ten marbles into the opposite point wins."],
         app=["2, 3, 4 or 6 players on one device.",
              "Any seat can be a person or the AI."]),
    dict(slug="animal-chess", name="Animal Chess", aka="Jungle · Dou Shou Qi · 斗兽棋", players="2 players",
         title="Animal Chess (Jungle, Dou Shou Qi 斗兽棋) Offline – Android",
         desc="Play Animal Chess, also called Jungle or Dou Shou Qi (斗兽棋), offline on Android against the AI or a friend. The childhood classic, free, no Wi-Fi needed.",
         intro="The childhood classic from China: eight animals a side on a 7×9 board with two rivers, traps and a den. The elephant rules the jungle, except that the tiny rat can bring it down.",
         rules=["From strongest to weakest: Elephant, Lion, Tiger, Leopard, Wolf, Dog, Cat, Rat.",
                "Animals move one square up, down, left or right, and capture an enemy of equal or lower rank.",
                "The Rat can capture the Elephant, but the Elephant cannot capture the Rat.",
                "Only the Rat may swim. Lions and Tigers leap across the river, unless a Rat in the water blocks the way.",
                "An enemy standing in one of your traps loses its rank, so any of your animals can take it.",
                "Walk into the opponent's den, or capture every enemy animal, to win."],
         app=["Every piece shows its rank, and a Ranks button explains them all.",
              "Play the AI at three levels or a friend on one device."]),
    dict(slug="luzhanqi", name="Luzhanqi", aka="Army Chess · Land Battle Chess · 陆战棋 · 军棋", players="2 players",
         title="Luzhanqi (Army Chess 军棋) Offline vs AI – Free Android App",
         desc="Play Luzhanqi, Chinese Army Chess (军棋 / 陆战棋), offline on Android: Hidden, Open and Flip rules against the AI. Free, no account needed.",
         intro="Chinese Army Chess: deploy twenty-five pieces with their ranks hidden, probe the enemy lines, and bluff your way to the opposing flag.",
         rules=["Each side deploys twenty-five pieces: officers from Field Marshal down to Engineer, plus bombs, landmines and a flag.",
                "When two pieces meet, the higher rank wins, and equal ranks remove each other.",
                "A bomb destroys whatever it meets, and itself with it.",
                "Landmines and the flag never move. Only an engineer can clear a landmine without being lost.",
                "Railways carry pieces a long way in a straight line, and engineers can turn corners on them. A piece in a camp cannot be attacked.",
                "Capture the enemy flag to win."],
         app=["Three ways to play: Hidden, Open and Flip.",
              "Arrange your own deployment or start from a random setup.",
              "The app settles every battle, so hidden ranks stay hidden with no referee needed."]),
    dict(slug="ludo", name="Ludo", aka="The family race game", players="2, 3 or 4 players",
         title="Ludo Offline – 2 to 4 Players vs AI or Friends on Android",
         desc="Play Ludo offline on Android with 2, 3 or 4 players: family and friends on one phone, the AI, or both. Free, no sign-in, no Wi-Fi needed.",
         intro="Roll the die, bring your four tokens out, run them round the board and get them all home before anyone else.",
         rules=["Roll a six to bring a token out of your yard.",
                "Move a token forward by the number you roll.",
                "Land on an opponent's token to send it back to its yard; tokens on safe squares cannot be captured.",
                "Get all four tokens home first to win."],
         app=["2, 3 or 4 players on one device.",
              "Any seat can be a person or the AI."]),
    dict(slug="aeroplane-chess", name="Aeroplane Chess", aka="Flying Chess · 飞行棋", players="2, 3 or 4 players",
         title="Aeroplane Chess (Flying Chess 飞行棋) Offline – Android",
         desc="Play Aeroplane Chess, Flying Chess (飞行棋), offline on Android with 2 to 4 players and the AI. Jumps, shortcut flights and captures. Free.",
         intro="China's favourite take on the Ludo race, with planes instead of tokens, and jumps and shortcut flights that can turn the game around in a single roll.",
         rules=["Roll a six to take a plane off from its hangar.",
                "Land on a square of your own colour to jump ahead to the next one.",
                "Some squares launch a shortcut flight straight across the board.",
                "Land on an opponent's plane to send it back to its hangar.",
                "Overshoot the finish and you bounce back. Fly all four planes home first to win."],
         app=["2, 3 or 4 players on one device.",
              "Any seat can be a person or the AI."]),
    dict(slug="yutnori", name="Yutnori", aka="Yut Nori · 윷놀이", players="2 players",
         title="Yutnori (윷놀이) Offline – Play Yut Nori vs AI on Android",
         desc="Play Yutnori (Yut Nori, 윷놀이), the traditional Korean stick-throwing game, offline on Android against the AI or a friend. Free, no account.",
         intro="Korea's traditional New Year game. Throw four yut sticks, race your markers around the board, and cut through the middle on the corner shortcuts.",
         rules=["Throw four sticks. The result moves you one to five spaces: Do (1), Gae (2), Geol (3), Yut (4) or Mo (5).",
                "Throwing Yut or Mo, or capturing an opponent's marker, earns another throw.",
                "Stop on a corner and you can take the diagonal shortcut through the centre.",
                "Markers that share a point travel together as a stack.",
                "Land on an opponent to send their markers back to the start. Bring all four markers home first to win."],
         app=["Four markers per side; tap the sticks to throw.",
              "Play the AI or a friend on one device."]),
]


# Long-form rules with diagrams, for the games whose rules are hardest to find written down. Every
# statement here was checked against the app's rules engine; keep it that way when editing.
DETAIL = {
    "animal-chess": dict(h2="Animal Chess rules in full", blocks=[
        ("h3", "The board"),
        ("p", "Animal Chess is played on a board seven squares wide and nine long. Two rivers, each two squares wide "
              "and three long, fill the middle. Each player has a den in the middle of their back row, with three "
              "traps around it."),
        ("figure", "jungle_board", "The opening position, Red at the top and Blue at the bottom. Numbers are ranks, "
                                   "from 8 for the Elephant down to 1 for the Rat. Blue squares are the rivers, ✕ "
                                   "squares are traps, and the dark arch is each side's den."),
        ("h3", "The animals"),
        ("table", ["Rank", "Animal", "Special power"], [
            [8, "Elephant", "Captures every animal except the Rat"],
            [7, "Lion", "Jumps over a river"],
            [6, "Tiger", "Jumps over a river"],
            [5, "Leopard", "–"],
            [4, "Wolf", "–"],
            [3, "Dog", "–"],
            [2, "Cat", "–"],
            [1, "Rat", "Swims in the river, and captures the Elephant"]]),
        ("h3", "Moving and capturing"),
        ("ul", ["Players take turns moving one animal one square up, down, left or right. Animals never move "
                "diagonally.",
                "Move onto an enemy animal to capture it. An animal can capture an enemy of the same rank or lower.",
                "The exception works both ways: the Rat can capture the Elephant, and the Elephant can never capture "
                "the Rat.",
                "No animal may enter its own den."]),
        ("h3", "Rivers"),
        ("figure", "jungle_river", "① The Lion jumps the river lengthwise. ② The Tiger jumps it crosswise. ③ A Rat "
                                   "in the water blocks the way, so this Lion cannot jump."),
        ("ul", ["Only the Rat can go into the water.",
                "A Rat in the water and an animal on land cannot capture each other. Two Rats in the water can.",
                "The Lion and the Tiger jump over a river in a straight line, lengthwise or crosswise, to the bank on "
                "the other side, and may capture an enemy standing there.",
                "Any Rat in the water along the way, yours or your opponent's, blocks the jump."]),
        ("h3", "Traps and dens"),
        ("ul", ["An enemy animal standing on one of your traps loses its rank, so any of your animals can capture "
                "it: even your Cat can take their Lion.",
                "Your own animals keep their full rank on your traps.",
                "Move any animal into your opponent's den and you win at once."]),
        ("h3", "Winning and draws"),
        ("ul", ["You win by entering the enemy den, by capturing every enemy animal, or when your opponent has no "
                "legal move.",
                "If the same position comes up five times with the same player to move, or both players make thirty "
                "moves without a capture, the app offers a draw. Accept it, or play on and the count starts again. "
                "Games between two AIs are drawn automatically."]),
        ("h3", "Tips for your first games"),
        ("ul", ["Guard your Rat: it is the only animal that can capture the enemy Elephant outside your traps.",
                "A Rat waiting in the water stops the enemy Lion and Tiger from jumping that river.",
                "An enemy that reaches your traps is easy to capture, so keep a defender near your den."]),
    ]),
    "luzhanqi": dict(h2="Luzhanqi rules in full", blocks=[
        ("h3", "The board"),
        ("p", "Each player has a half of five columns and six rows. Pieces stand on posts joined by roads and "
              "railways. Five round camps sit in the middle of each half, and two headquarters in the back row."),
        ("figure", "luzhanqi_board", "① Headquarters. ② Camps. ③ The front: the halves meet at only three "
                                     "crossings, railways on the left and right and a road in the middle; mountains "
                                     "block the other two columns."),
        ("legend", [("post", "Post"),
                    ("camp", "Camp: a piece inside cannot be attacked"),
                    ("hq", "Headquarters: the flag starts here, and a piece that enters can no longer move"),
                    ("road", "Road: one step at a time"),
                    ("rail", "Railway: any distance in a straight line"),
                    ("mountain", "Mountain: no way through")]),
        ("h3", "The pieces"),
        ("p", "Each side has twenty-five pieces, which fill every post in its half except the five camps."),
        ("table", ["Piece", "Rank", "Each side", "Notes"], [
            ["Marshal", 9, 1, "When it falls, the position of its side's flag is revealed"],
            ["General", 8, 1, ""],
            ["Major General", 7, 2, ""],
            ["Brigadier", 6, 2, ""],
            ["Colonel", 5, 2, ""],
            ["Major", 4, 2, ""],
            ["Captain", 3, 3, ""],
            ["Lieutenant", 2, 3, ""],
            ["Engineer", 1, 3, "Clears landmines, and turns corners on the railway"],
            ["Bomb", "–", 2, "Removes whatever it meets, and itself"],
            ["Landmine", "–", 3, "Never moves; removes any attacker except an Engineer"],
            ["Flag", "–", 1, "Never moves; lose it and you lose the game"]]),
        ("h3", "Deployment"),
        ("ul", ["The flag must stand in one of your two headquarters.",
                "Landmines may only go in your back two rows.",
                "Bombs may not go in your front row.",
                "In Hidden and Open games you arrange your own army or start from a random setup. In Flip games all "
                "fifty pieces are shuffled face down across both halves."]),
        ("h3", "Moving"),
        ("ul", ["On a road a piece moves one step to the next post, including the diagonal roads into and out of "
                "camps.",
                "On a railway a piece moves any distance in a straight line, as long as no piece stands in the way. "
                "Only the Engineer may turn corners on the railway.",
                "Landmines and the flag never move, and a piece that enters a headquarters stays there for the rest "
                "of the game.",
                "A piece may move into an empty camp, and a piece inside a camp cannot be attacked."]),
        ("h3", "Battles"),
        ("ul", ["Move onto an enemy piece to attack it. The higher rank wins and stays; equal ranks remove each other.",
                "A bomb and whatever it meets are both removed, whichever side attacked.",
                "An Engineer that attacks a landmine clears it and takes its post. Any other piece that attacks a "
                "landmine is removed together with it.",
                "Any piece that reaches the enemy flag captures it and wins the game."]),
        ("h3", "Hidden, Open and Flip"),
        ("ul", ["Hidden: you see your own pieces, not your opponent's. A piece that wins a battle is revealed.",
                "Open: both players see every piece.",
                "Flip: every piece starts face down. On your turn, either turn one face-down piece over, which uses "
                "the turn, or move one of your own face-up pieces. Face-down pieces cannot be attacked."]),
        ("h3", "Winning and draws"),
        ("ul", ["Capture the enemy flag, or leave your opponent with no piece that can move.",
                "The app declares a draw when the same position comes up three times with the same player to move, "
                "or both players make forty moves without a battle or a flip."]),
    ]),
    "aeroplane-chess": dict(h2="Aeroplane Chess rules in full", blocks=[
        ("h3", "The board"),
        ("p", "Each of the four colours, red, yellow, green and blue, has four planes, a hangar in one corner, and "
              "a home stretch of six cells leading to the goal in the centre. A shared track of 52 cells runs round "
              "the board, coloured red, yellow, blue and green in turn. Two, three or four can play, and any seat "
              "can be the AI."),
        ("figure", "aeroplane_route", "Red's route, laid out in rows. ① Land on your own colour and you jump four "
                                      "cells to the next one. ② A jump onto the flight cell flies on: 13 → 17 → 29 "
                                      "→ 33. ③ Cell 49 turns into the home stretch, 50 to 55, and the goal is 56."),
        ("h3", "Taking off"),
        ("ul", ["A plane leaves its hangar only on a 6, and moves to its launch pad (0 on the diagram).",
                "A 6 can instead move a plane that is already out six cells forward. Either way, roll again after "
                "a 6.",
                "You must move if any plane can; if none can, the turn passes."]),
        ("h3", "Jumps and flights"),
        ("ul", ["Land on a cell of your own colour and the plane jumps four cells to the next one. It jumps only "
                "once per move.",
                "Your 17th cell is the flight cell. Land on it and the plane flies across the board to your 29th "
                "cell, then jumps four more to the 33rd.",
                "A jump that lands on the flight cell takes the flight as well.",
                "Your last cell of your own colour, the 49th, turns into the home stretch instead of jumping."]),
        ("h3", "Sending planes home"),
        ("ul", ["Land on a cell with opponents' planes and all of them go back to their hangars. The same happens "
                "on every cell where a jump or a flight comes down.",
                "Planes on a home stretch are safe, with one exception: each flight passes over one cell of another "
                "colour's home stretch, and a plane waiting there is sent home."]),
        ("h3", "Getting home"),
        ("ul", ["A plane needs the exact number to reach the goal. Roll too high and it reaches the goal, then "
                "goes back by the steps left over.",
                "The first player to bring all four planes home wins."]),
    ]),
    "yutnori": dict(h2="Yutnori rules in full", blocks=[
        ("h3", "The board"),
        ("p", "The Yutnori board has 29 points: twenty round the edge and nine on two diagonals that cross in the "
              "centre. Pieces start off the board, go anticlockwise round the edge from the start corner, and leave "
              "the board after passing it again."),
        ("figure", "yutnori_board", "① The start and finish corner. ② The first corner, Mo (모), and ③ the "
                                    "second, Dwitmo (뒷모): stop on either to take a shortcut. ④ The centre, Bang "
                                    "(방). Arrows show the direction of travel."),
        ("h3", "The yut sticks"),
        ("p", "Each turn you throw four sticks, flat on one side and rounded on the other. The number of flat sides "
              "facing up decides the move."),
        ("table", ["Throw", "Flat sides up", "Steps", "Throw again?"], [
            ["Do (도)", 1, 1, "No"],
            ["Gae (개)", 2, 2, "No"],
            ["Geol (걸)", 3, 3, "No"],
            ["Yut (윷)", 4, 4, "Yes"],
            ["Mo (모)", "0, all rounded sides up", 5, "Yes"]]),
        ("p", "The app plays without Back Do (빽도), the house rule in which one marked stick moves a piece a step "
              "backwards."),
        ("h3", "Moving"),
        ("ul", ["Throw first, then choose a piece to move: a new one from off the board, or one already on it.",
                "A new piece's first step takes it to the point just after the start corner.",
                "Use your current throw before you take an extra throw.",
                "A piece that lands on the start corner needs one more step to get home, and a throw that carries "
                "it past the corner takes it home."]),
        ("h3", "Shortcuts"),
        ("ul", ["Stop exactly on the first corner (②) and your next move takes the diagonal through the centre.",
                "Stop exactly on the second corner (③) and your next move takes the other diagonal, through the "
                "centre and straight to the start corner.",
                "Stop exactly on the centre (④) and your next move heads straight for the start corner.",
                "A piece that only passes over a corner or the centre carries on the way it was going.",
                "The quickest way home is a Mo to the first corner, a Geol to the centre, then a Yut."]),
        ("h3", "Stacking and capturing"),
        ("ul", ["Land on your own piece and the two stack. From then on the stack moves as one.",
                "Land on an opponent and every piece on that point goes back off the board, and you throw again.",
                "A Yut or Mo that also captures earns one extra throw, not two."]),
        ("h3", "Winning"),
        ("p", "The app plays Yutnori for two, with four pieces each. The first player to bring all four pieces home "
              "wins."),
    ]),
}
