v = "Matutino"

print(len(v))


    def post(self, request, *args, **kwargs):
        registrar_nuevo_uni(
            self= self,
            nombre = ,
            user = self.request.user,
        )

        return HttpResponseRedirect(
            reverse(
                'admins_app:universo'
            )
        )


?page=


           "{% url 'personal_app:personal-detail' p.id %}
import requests

data=requests.get('https://randomuser.me/api/')
for d in data:
    print(d)

