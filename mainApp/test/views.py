from rest_framework import generics
from rest_framework.response import Response
from .models import Test, Question, Answer
from .serializers import TestSerializer, QuestionSerializer, AnswerSerializer

class TestListCreateView(generics.ListCreateAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer

class TestDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer

class TestStatsView(generics.RetrieveAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        pass_count = instance.pass_count
        total_count = instance.tests_taken.count()
        success_percentage = (pass_count / total_count) * 100 if total_count > 0 else 0
        hardest_question = Question.objects.filter(test=instance).order_by('-difficulty').first()

        data = {
            'pass_count': pass_count,
            'success_percentage': success_percentage,
            'hardest_question': hardest_question.text if hardest_question else None,
        }
        return Response(data)


class QuestionListCreateView(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class QuestionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class AnswerListCreateView(generics.ListCreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

class AnswerDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
