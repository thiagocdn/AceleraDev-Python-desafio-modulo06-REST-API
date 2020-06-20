from collections import Counter

from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['POST'])
def lambda_function(request):
    request_data = request.data.get('question')

    counter = Counter()
    for number in request_data:
        counter[number] += 1

    solution = []

    for item in counter.most_common():
        for _ in range(item[1]):
            solution.append(item[0])

    return Response({"solution": solution})
