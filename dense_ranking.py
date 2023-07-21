def get_dense_ranking(scores):
    ranking = []
    current_rank = 1
    for i in range(len(scores)):
        if i > 0 and scores[i] != scores[i - 1]:
            current_rank += 1
        ranking.append(current_rank)
    return ranking

def main():
    num_players = int(input("Masukkan jumlah pemain: "))
    scores = list(map(int, input("Masukkan skor pemain (dipisahkan oleh spasi): ").split()))
    num_games = int(input("Masukkan jumlah permainan GITS: "))
    for _ in range(num_games):
        gits_scores = list(map(int, input("Masukkan skor GITS dalam satu permainan (dipisahkan oleh spasi): ").split()))
        all_scores = sorted(scores + gits_scores, reverse=True)
        gits_ranks = get_dense_ranking(all_scores[:num_players + len(gits_scores)])
        print(*gits_ranks[num_players:num_players + len(gits_scores)])

if __name__ == "__main__":
    main()
