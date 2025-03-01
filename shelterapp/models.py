from django.db import models
from django.contrib.auth.models import User

class Shelter(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    photo = models.ImageField(upload_to='shelter_photos/', blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='shelters')

    def __str__(self):
        return self.name
    
class Role(models.Model):
    ADMIN = 'Admin'
    USER = 'User'
    ROLE_CHOICES = [
        (ADMIN, 'Admin'),
        (USER, 'User'),
    ]
    name = models.CharField(max_length=50, choices=ROLE_CHOICES, unique=True)

    def __str__(self):
        return self.name
    
class UserShelter(models.Model):
        user = models.ForeignKey(User, on_delete=models.CASCADE)
        shelter = models.ForeignKey(Shelter, on_delete=models.CASCADE)
        class Meta:
            unique_together = ('user', 'shelter')
            
class UserRole(models.Model):
        user = models.ForeignKey(User, on_delete=models.CASCADE)
        role = models.ForeignKey(Role, on_delete=models.CASCADE)
        class Meta:
            unique_together = ('user', 'role')

        def __str__(self):
            return f"{self.user.username} - {self.role.name}"
            
class VetAssignment(models.Model):
    diagnosis = models.CharField(max_length=255, blank=True, null=True, verbose_name='Диагноз')
    medication = models.CharField(max_length=255, blank=True, null=True, verbose_name='Необходимые лекарства')
    dosage = models.CharField(max_length=50, blank=True, null=True, verbose_name='Дозировка в граммах')
    frequency = models.CharField(max_length=50, blank=True, null=True, verbose_name='Сколько раз в день')
    duration = models.CharField(max_length=50, blank=True, null=True, verbose_name='Продолжительность лечения')
    document = models.FileField(upload_to='vet_documents/', blank=True, null=True, verbose_name='Документ')

    def __str__(self):
        return f"{self.diagnosis} - {self.medication}"
    
    
class Pet(models.Model):
    CATEGORY_CHOICES = [
        ('Домашнее', 'Домашнее'),
        ('Дикое', 'Дикое'),
    ]
    
    FAMILY_CHOICES = {
        'Домашнее': [
            ('Кошки', 'Кошки'),
            ('Собаки', 'Собаки'),
            ('Парнокопытные-Коровы','Парнокопытные-Коровы'),
            ('Парнокопытные-Овцы','Парнокопытные-Овцы'),
            ('Парнокопытные-Козы','Парнокопытные-Козы'),
            ('Парнокопытные-Буйволы','Парнокопытные-Буйволы'),
            ('Парнокопытные-Дромедары','Парнокопытные-Дромедары'),
            ('Парнокопытные-Бактрианы','Парнокопытные-Бактрианы'),
            ('Парнокопытные-Ламы','Парнокопытные-Ламы'),
            ('Парнокопытные-Альпаки','Парнокопытные-Альпаки'),
            ('Парнокопытные-Северные олени','Парнокопытные-Северные олени'),
            ('Непарнокопытные-Лошади','Непарнокопытные-Лошади'),
            ('Непарнокопытные-Ослы','Непарнокопытные-Ослы'),
            ('Непарнокопытные-Пони','Непарнокопытные-Пони'),
            ('Кролики','Кролики'),
            ('Грызуны', 'Грызуны'),
            ('Фретка', 'Фретка'),
            ('Птицы-курообразные', 'Птицы-курообразные'),
            ('Птицы-гусеобразные', 'Птицы-гусеобразные'),
            ('Птицы-голубеобразные', 'Птицы-голубеобразные'),
        ],
        'Дикое': [
            ('Рептилии', 'Рептилии'),
            ('Другое', 'Другое'),
        ],
    }
    
    BREED_CHOICES = {
        'Кошки': [
            ('Абиссинская','Абиссинская'),
            ('Австралийский мист','Австралийский мист'),
            ('Азиатская','Азиатская'),
            ('Американская жесткошерстная','Американская жесткошерстная'),
            ('Американский керл','Американский керл'),
            ('Балийская','Балийская'),
            ('Беспородная кошка','Беспородная кошка'),
            ('Бенгальская','Бенгальская'),
            ('Бирманская','Бирманская'),
            ('Бомбейская','Бомбейская'),
            ('Британская длинношерстная','Британская длинношерстная'),
            ('Британская короткошерстная','Британская короткошерстная'),
            ('Бурманская','Бурманская'),
            ('Бурмилла','Бурмилла'),
            ('Гавана','Гавана'),
            ('Девон-рекс','Девон-рекс'),
            ('Египетский мау','Египетский мау'),
            ('Камышовая','Камышовая'),
            ('Као-мани','Као-мани'),
            ('Кимрик','Кимрик'),
            ('Корат','Корат'),
            ('Корниш-рекс','Корниш-рекс'),
            ('Лаперм','Лаперм'),
            ('Манчкин','Манчкин'),
            ('Мейн-кун', 'Мейн-кун'),
            ('Мэнкс','Мэнкс'),
            ('Нибелунг','Нибелунг'),
            ('Норвежская лесная','Норвежская лесная'),
            ('Ориентальная (восточная) длинношерстная','Ориентальная (восточная) длинношерстная'),
            ('Ориентальная (восточная) короткошерстная','Ориентальная (восточная) короткошерстная'),
            ('Оцикет','Оцикет'),
            ('Персидская длинношерстная','Персидская длинношерстная'),
            ('Пиксибоб','Пиксибоб'),
            ('Русская голубая','Русская голубая'),
            ('Рэгдолл','Рэгдолл'),
            ('Саванна','Саванна'),
            ('Селкирк-рекс','Селкирк-рекс'),
            ('Сиамская', 'Сиамская'),
            ('Сибирская лесная','Сибирская лесная'),
            ('Сингапура','Сингапура'),
            ('Сноу-шу','Сноу-шу'),
            ('Сомалийская','Сомалийская'),
            ('Сфинкс', 'Сфинкс'),
            ('Тайская','Тайская'),
            ('Тойгер','Тойгер'),
            ('Тонкинская','Тонкинская'),
            ('Турецкий ван','Турецкий ван'),
            ('Хайленд-страйт','Хайленд-страйт'),
            ('Шантильи-тиффани','Шантильи-тиффани'),
            ('Шартрез','Шартрез'),
            ('Шиншилла','Шиншилла'),
            ('Шотландская вислоухая','Шотландская вислоухая'),
            ('Шотландская прямоухая','Шотландская прямоухая'),
            ('Экзотическая короткошерстная','Экзотическая короткошерстная'),
            ('Японский бобтейл длинношерстный','Японский бобтейл длинношерстный'),
            ('Японский бобтейл короткошерстный','Японский бобтейл короткошерстный'),
        ],
        
        'Собаки': [
            ('Австралийская овчарка','Австралийская овчарка'),
            ('Австралийская пастушья собака','Австралийская пастушья собака'),
            ('Азавак','Азавак'),
            ('Акита-ину','Акита-ину'),
            ('Алабай','Алабай'),
            ('Аляскинский кли-кай','Аляскинский кли-кай'),
            ('Аляскинский маламут','Аляскинский маламут'),
            ('Американская акита','Американская акита'),
            ('Американский бандог','Американский бандог'),
            ('Американский булли','Американский булли'),
            ('Американский бульдог','Американский бульдог'),
            ('Американский голый терьер','Американский голый терьер'),
            ('Американский кокер-спаниель','Американский кокер-спаниель'),
            ('Американский стаффордширский терьер','Американский стаффордширский терьер'),
            ('Английский бульдог','Английский бульдог'),
            ('Английский кокер-спаниель','Английский кокер-спаниель'),
            ('Английский мастиф','Английский мастиф'),
            ('Английский пойнтер','Английский пойнтер'),
            ('Английский сеттер','Английский сеттер'),
            ('Английский той-терьер','Английский той-терьер'),
            ('Английский фоксхаунд','Английский фоксхаунд'),
            ('Аппенцеллер зенненхунд','Аппенцеллер зенненхунд'),
            ('Аргентинский дог','Аргентинский дог'),
            ('Афганская борзая','Афганская борзая'),
            ('Аффенпинчер','Аффенпинчер'),
            ('Банхар','Банхар'),
            ('Басенджи','Басенджи'),
            ('Бассет-хаунд','Бассет-хаунд'),
            ('Бедлингтон-терьер','Бедлингтон-терьер'),
            ('Белая швейцарская овчарка','Белая швейцарская овчарка'),
            ('Беспородная собака','Беспородная собака'),
            ('Бельгийская овчарка','Бельгийская овчарка'),
            ('Бельгийский гриффон','Бельгийский гриффон'),
            ('Бернский зенненхунд','Бернский зенненхунд'),
            ('Бивер-йоркширский терьер','Бивер-йоркширский терьер'),
            ('Бигль','Бигль'),
            ('Бишон фризе','Бишон фризе'),
            ('Бладхаунд','Бладхаунд'),
            ('Бобтейл','Бобтейл'),
            ('Боксер','Боксер'),
            ('Большой швейцарский зенненхунд','Большой швейцарский зенненхунд'),
            ('Бордер-колли','Бордер-колли'),
            ('Бордер-терьер','Бордер-терьер'),
            ('Бордоский дог','Бордоский дог'),
            ('Босерон','Босерон'),
            ('Бостон-терьер','Бостон-терьер'),
            ('Бретонский эпаньоль','Бретонский эпаньоль'),
            ('Бриар','Бриар'),
            ('Брюссельский гриффон','Брюссельский гриффон'),
            ('Бульмастиф','Бульмастиф'),
            ('Бультерьер','Бультерьер'),
            ('Бурбуль','Бурбуль'),
            ('Веймаранер','Веймаранер'),
            ('Вельш-корги кардиган','Вельш-корги кардиган'),
            ('Вельш-корги пемброк','Вельш-корги пемброк'),
            ('Вельштерьер','Вельштерьер'),
            ('Венгерская выжла','Венгерская выжла'),
            ('Вест-хайленд-уайт-терьер','Вест-хайленд-уайт-терьер'),
            ('Восточно-сибирская лайка','Восточно-сибирская лайка'),
            ('Восточноевропейская овчарка','Восточноевропейская овчарка'),
            ('Гаванский бишон','Гаванский бишон'),
            ('Гампр','Гампр'),
            ('Грейхаунд','Грейхаунд'),
            ('Далматин','Далматин'),
            ('Джек-рассел-терьер','Джек-рассел-терьер'),
            ('Дирхаунд','Дирхаунд'),
            ('Доберман','Доберман'),
            ('Дратхаар','Дратхаар'),
            ('Западно-сибирская лайка','Западно-сибирская лайка'),
            ('Золотистый ретривер','Золотистый ретривер'),
            ('Ирландский водяной спаниель','Ирландский водяной спаниель'),
            ('Ирландский волкодав','Ирландский волкодав'),
            ('Ирландский сеттер','Ирландский сеттер'),
            ('Ирландский терьер','Ирландский терьер'),
            ('Испанский мастиф','Испанский мастиф'),
            ('Йоркширский терьер','Йоркширский терьер'),
            ('Ка-де-бо','Ка-де-бо'),
            ('Кавалер-кинг-чарльз-спаниель','Кавалер-кинг-чарльз-спаниель'),
            ('Кавказская овчарка','Кавказская овчарка'),
            ('Канарский дог','Канарский дог'),
            ('Кангал','Кангал'),
            ('Кане-корсо','Кане-корсо'),
            ('Карело-финская лайка','Карело-финская лайка'),
            ('Карельская медвежья собака','Карельская медвежья собака'),
            ('Карликовая такса','Карликовая такса'),
            ('Кеесхонд','Кеесхонд'),
            ('Керн-терьер','Керн-терьер'),
            ('Керри-блю-терьер','Керри-блю-терьер'),
            ('Китайская хохлатая собака','Китайская хохлатая собака'),
            ('Коикерхондье','Коикерхондье'),
            ('Кокапу','Кокапу'),
            ('комондор','Комондор'),
            ('Котон-де-тулеар','Котон-де-тулеар'),
            ('Кроличья такса','Кроличья такса'),
            ('Ксолоитцкуинтли','Ксолоитцкуинтли'),
            ('Курцхаар','Курцхаар'),
            ('Курчавошерстный ретривер','Курчавошерстный ретривер'),
            ('Лабрадор-ретривер','Лабрадор-ретривер'),
            ('Левретка','Левретка'),
            ('Леонбергер','Леонбергер'),
            ('Лхаса апсо','Лхаса апсо'),
            ('Малинуа','Малинуа'),
            ('Мальтийская болонка','Мальтийская болонка'),
            ('Мальтипу','Мальтипу'),
            ('Манчестер-терьер','Манчестер-терьер'),
            ('Маремма-абруццкая овчарка','Маремма-абруццкая овчарка'),
            ('Мини-бультерьер','Мини-бультерьер'),
            ('Миттельшнауцер','Миттельшнауцер'),
            ('Мопс','Мопс'),
            ('Московская сторожевая','Московская сторожевая'),
            ('Московский дракон','Московский дракон'),
            ('Неаполитанский мастиф','Неаполитанский мастиф'),
            ('Немецкая овчарка', 'Немецкая овчарка'),
            ('Немецкий дог','Немецкий дог'),
            ('Немецкий пинчер','Немецкий пинчер'),
            ('Немецкий ягдтерьер','Немецкий ягдтерьер'),
            ('Новошотландский ретривер','Новошотландский ретривер'),
            ('Норвежский лундехунд','Норвежский лундехунд'),
            ('Норвич-терьер','Норвич-терьер'),
            ('Ньюфаундленд','Ньюфаундленд'),
            ('Пагль','Пагль'),
            ('Папильон','Папильон'),
            ('Парсон-рассел-терьер','Парсон-рассел-терьер'),
            ('Пекинес','Пекинес'),
            ('Перуанская голая','Перуанская голая'),
            ('Петербургская орхидея','Петербургская орхидея'),
            ('Пиренейская горная','Пиренейская горная'),
            ('Питбуль','Питбуль'),
            ('Померанский шпиц','Померанский шпиц'),
            ('Помски','Помски'),
            ('Португальская водяная','Португальская водяная'),
            ('Пражский крысарик','Пражский крысарик'),
            ('Пти-брабансон','Пти-брабансон'),
            ('Пудель','Пудель'),
            ('Пхунсан','Пхунсан'),
            ('Ризеншнауцер','Ризеншнауцер'),
            ('Родезийский риджбек','Родезийский риджбек'),
            ('Ротвейлер','Ротвейлер'),
            ('Русская гончая','Русская гончая'),
            ('Русская каштанка','Русская каштанка'),
            ('Русская пегая гончая','Русская пегая гончая'),
            ('Русская псовая борзая','Русская псовая борзая'),
            ('Русская цветная болонка','Русская цветная болонка'),
            ('Русский охотничий спаниель','Русский охотничий спаниель'),
            ('Русский той-терьер','Русский той-терьер'),
            ('Русский черный терьер','Русский черный терьер'),
            ('Русско-европейская лайка','Русско-европейская лайка'),
            ('Салюки','Салюки'),
            ('Самоед','Самоед'),
            ('Сахалинский хаски','Сахалинский хаски'),
            ('Сенбернар','Сенбернар'),
            ('Сиба-ину','Сиба-ину'),
            ('Сибирский хаски','Сибирский хаски'),
            ('Скай-терьер','Скай-терьер'),
            ('Скотч-терьер','Скотч-терьер'),
            ('Стаффордширский бультерьер','Стаффордширский бультерьер'),
            ('Тайский риджбек','Тайский риджбек'),
            ('Такса','Такса'),
            ('Тибетский мастиф','Тибетский мастиф'),
            ('Тибетский спаниель','Тибетский спаниель'),
            ('Той-фокстерьер','Той-фокстерьер'),
            ('Тоса-ину','Тоса-ину'),
            ('Уиппет','Уиппет'),
            ('Фараонова собака','Фараонова собака'),
            ('Фокстерьер','Фокстерьер'),
            ('Французский бульдог', 'Французский бульдог'),
            ('Хотошо','Хотошо'),
            ('Цвергпинчер','Цвергпинчер'),
            ('Цвергшнауцер','Цвергшнауцер'),
            ('Чау-чау','Чау-чау'),
            ('Чесапик-бей-ретривер','Чесапик-бей-ретривер'),
            ('Чехословацкий волчак','Чехословацкий волчак'),
            ('Чирнеко дель Этна','Чирнеко дель Этна'),
            ('Чихуахуа','Чихуахуа'),
            ('Шарпей','Шарпей'),
            ('Шелти','Шелти'),
            ('Ши-тцу','Ши-тцу'),
            ('Шипперке','Шипперке'),
            ('Шотландская овчарка(колли)','Шотландская овчарка(колли)'),
            ('Шотландский сеттер','Шотландский сеттер'),
            ('Энтлебухер зенненхунд','Энтлебухер зенненхунд'),
            ('Эрдельтерьер','Эрдельтерьер'),
            ('Эстонская гончая','Эстонская гончая'),
            ('Южнорусская овчарка','Южнорусская овчарка'),
            ('Якутская лайка','Якутская лайка'),
            ('Японский хин','Японский хин'),
            ('Японский шпиц','Японский шпиц'),
        ],
        'Парнокопытные-Коровы': [
            ('Ангусская (Абердин-ангусская)','Ангусская (Абердин-ангусская)'),
            ('Абигар','Абигар'),
            ('Айрширская','Айрширская'),
            ('Акауши (Японская коричневая)','Акауши (Японская коричневая)'),
            ('Англерская','Англерская'),
            ('Бестужевская','Бестужевская'),
            ('Галловейская','Галловейская'),
            ('Герефордская','Герефордская'),
            ('Гернзейская','Гернзейская'),
            ('Голштинская','Голштинская'),
            ('Горный скот Дагестана','Горный скот Дагестана'),
            ('Джерсейская','Джерсейская'),
            ('Истобенская','Истобенская'),
            ('Красная датская','Красная датская'),
            ('Красная шведская','Красная шведская'),
            ('Красная степная','Красная степная'),
            ('Красная горбатовская','Красная горбатовская'),
            ('Красная тамбовская','Красная тамбовская'),
            ('Красно-пестрая','Красно-пестрая'),
            ('Казахская белоголовая','Казахская белоголовая'),
            ('Калмыцкая','Калмыцкая'),
            ('Кианская','Кианская'),
            ('Костромская','Костромская'),
            ('Лимузинская','Лимузинская'),
            ('Мен-анжу','Мен-анжу'),
            ('Монбельярдская','Монбельярдская'),
            ('Обрак','Обрак'),
            ('Русская комолая','Русская комолая'),
            ('Салерс','Салерс'),
            ('Санта-гертруда','Санта-гертруда'),
            ('Сибирячка','Сибирячка'),
            ('Симментальская','Симментальская'),
            ('Суксунская','Суксунская'),
            ('Сычевская','Сычевская'),
            ('Тагильская','Тагильская'),
            ('Холмогорская','Холмогорская'),
            ('Черно-пестрая','Черно-пестрая'),
            ('Шаролезская','Шаролезская'),
            ('Швицкая','Швицкая'),
            ('Шортгорнская','Шортгорнская'),
            ('Ярославская','Ярославская'),
            ('Якутский скот','Якутский скот'),
        ],
        'Парнокопытные-Овцы': [
            ('Авасси','Авасси'),
            ('Австралийский меринос','Австралийский меринос'),
            ('Азербайджанский горный меринос','Азербайджанский горный меринос'),
            ('Акжайыкская','Акжайыкская'),
            ('Алтайская','Алтайская'),
            ('Апшеронская','Апшеронская'),
            ('Армянская полугрубошерстная','Армянская полугрубошерстная'),
            ('Архаромеринос','Архаромеринос'),
            ('Асканийская','Асканийская'),
            ('Ассаф','Ассаф'),
            ('Боререй','Боререй'),
            ('Гемпширская','Гемпширская'),
            ('Гиссарская','Гиссарская'),
            ('Грубошерстная померанская','Грубошерстная померанская'),
            ('Дегересская','Дегересская'),
            ('Дорпер','Дорпер'),
            ('Жанааркинская','Жанааркинская'),
            ('Исландская','Исландская'),
            ('Кавказская','Кавказская'),
            ('Карабахская','Карабахская'),
            ('Каракульская','Каракульская'),
            ('Карачаевская','Карачаевская'),
            ('Катумская','Катумская'),
            ('Курдючная порода','Курдючная порода'),
            ('Меринос','Меринос'),
            ('Мэнский лохтан','Мэнский лохтан'),
            ('Прекос','Прекос'),
            ('Рамбулье','Рамбулье'),
            ('Рацка','Рацка'),
            ('Решетиловская','Решетиловская'),
            ('Романовская','Романовская'),
            ('Сараджинская','Сараджинская'),
            ('Североевропейская короткохвостая','Североевропейская короткохвостая'),
            ('Североказахский меринос','Североказахский меринос'),
            ('Сокольская','Сокольская'),
            ('Сомалийская','Сомалийская'),
            ('Фарерская','Фарерская'),
            ('Хиосская','Хиосская'),
            ('Цвартблес','Цвартблес'),
            ('Эдильбаевская','Эдильбаевская'),
            ('Эстонская белоголовая','Эстонская белоголовая'),
            ('Эстонская темноголовая','Эстонская темноголовая'),
            ('Южноказахский меринос','Южноказахский меринос'),
        ],
        'Парнокопытные-Козы': [
            ('Абергельская','Абергельская'),
            ('Абхазская','Абхазская'),
            ('Австралийская коричневая','Австралийская коричневая'),
            ('Австралийская черная','Австралийская черная'),
            ('Австралийская миниатюрная','Австралийская миниатюрная'),
            ('Австралийская зааненская','Австралийская зааненская'),
            ('Аданайская','Аданайская'),
            ('Адани','Адани'),
            ('Азербайджанская грубошерстная','Азербайджанская грубошерстная'),
            ('Азпи-горри','Азпи-горри'),
            ('Акьябская','Акьябская'),
            ('Аквильская','Аквильская'),
            ('Алашаньская пуховая','Алашаньская пуховая'),
            ('Албанская','Албанская'),
            ('Албанская альпина','Албанская альпина'),
            ('Албас','Албас'),
            ('Алгарвиа','Алгарвиа'),
            ('Альпийская','Альпийская'),
            ('Альпийская коричневая','Альпийская коричневая'),
            ('Альпина полихрома','Альпина полихрома'),
            ('Алтайская горная','Алтайская горная'),
            ('Алтайская красная','Алтайская красная'),
            ('Аморгосская','Аморгосская'),
            ('Анатолийская черная','Анатолийская черная'),
            ('Андалузская черная горная','Андалузская черная горная'),
            ('Англо-нубийская','Англо-нубийская'),
            ('Ангорская','Ангорская'),
            ('Аппенцелльская','Аппенцелльская'),
            ('Арабская Иран','Арабская Иран'),
            ('Арабская Алжир','Арабская Алжир'),
            ('Аравийская','Аравийская'),
            ('Аранитасская белобокая','Аранитасская белобокая'),
            ('Аридейская','Аридейская'),
            ('Армянская грубошерстная','Армянская грубошерстная'),
            ('Ардийская','Ардийская'),
            ('Арси-Балеская','Арси-Балеская'),
            ('Асмарская','Асмарская'),
            ('Аспромонтская','Аспромонтская'),
            ('Ассам-хилл','Ассам-хилл'),
            ('Асвадская','Асвадская'),
            ('Афарская','Афарская'),
            ('Африканский пигмей','Африканский пигмей'),
            ('Ахтальская','Ахтальская'),
            ('Белая русская','Белая русская'),
            ('Бёрская','Бёрская'),
            ('Бенгальская','Бенгальская'),
            ('Бушская','Бушская'),
            ('Баварская лесная','Баварская лесная'),
            ('Бади','Бади'),
            ('Бетал','Бетал'),
            ('Баракеская','Баракеская'),
            ('Балканская','Балканская'),
            ('Бургунская','Бургунская'),
            ('Бурятская','Бурятская'),
            ('Бьяла','Бьяла'),
            ('Валашская','Валашская'),
            ('Вахшская','Вахшская'),
            ('Вятская','Вятская'),
            ('Витебская','Витебская'),
            ('Восточно-африканская','Восточно-африканская'),
            ('Венгерская','Венгерская'),
            ('Визацкая','Визацкая'),
            ('Вишнёвская','Вишневская'),
            ('Вади','Вади'),
            ('Виттель','Виттель'),
            ('Ванская','Ванская'),
            ('Гёргенская','Гёргенская'),
            ('Гранада','Гранада'),
            ('Германская белая благородная',''),
            ('Гуджарати','Гуджарати'),
            ('Ганди','Ганди'),
            ('Гёйгёльская','Гёйгёльская'),
            ('Гассанская','Гассанская'),
            ('Галлийская','Галлийская'),
            ('Гассаба','Гассаба'),
            ('Гиссарская','Гиссарская'),
            ('Галлуресская','Галлуресская'),
            ('Гаргеру','Гаргеру'),
            ('Гаргарская','Гаргарская'),
            ('Дамасская','Дамасская'),
            ('Донская','Донская'),
            ('Джамнапари','Джамнапари'),
            ('Дорсет','Дорсет'),
            ('Джакоб','Джакоб'),
            ('Дагестанская','Дагестанская'),
            ('Давлет','Давлет'),
            ('Дарлагская','Дарлагская'),
            ('Дельта','Дельта'),
            ('Дейримская','Дейримская'),
            ('Джабал Наффаса','Джабал Наффаса'),
            ('Диарбекская','Диарбекская'),
            ('Денг','Денг'),
            ('Египетская','Египетская'),
            ('Ербешка','Ербешка'),
            ('Енисейская','Енисейская'),
            ('Едильбайская','Едильбайская'),
            ('Еме','Еме'),
            ('Евроазиатская','Евроазиатская'),
            ('Еленина','Еленина'),
            ('Ёнченгская','Ёнченгская'),
            ('Жезказганская','Жезказганская'),
            ('Жупа','Жупа'),
            ('Жуа','Жуа'),
            ('Жабарская','Жабарская'),
            ('Зааненская','Зааненская'),
            ('Занзибарская','Занзибарская'),
            ('Залакарайская','Залакарайская'),
            ('Землянская','Землянская'),
            ('Загорская белая','Загорская белая'),
            ('Зулусская','Зулусская'),
            ('Зее','Зее'),
            ('Зугская','Зугская'),
            ('Испанская','Испанская'),
            ('Ивдельская','Ивдельская'),
            ('Иллирийская','Иллирийская'),
            ('Иранская','Иранская'),
            ('Ишковская','Ишковская'),
            ('Исаки','Исаки'),
            ('Ибаррская','Ибаррская'),
            ('Ик','Ик'),
            ('Иль де Франс','Иль де Франс'),
            ('Камерунская','Камерунская'),
            ('Калахарская красная','Калахарская красная'),
            ('Кашмирская','Кашмирская'),
            ('Кико','Кико'),
            ('Карликовая нигерийская','Карликовая нигерийская'),
            ('Курдская','Курдская'),
            ('Кубанская','Кубанская'),
            ('Карачаевская','Карачаевская'),
            ('Кипрская','Кипрская'),
            ('Кабардинская','Кабардинская'),
            ('Катта','Катта'),
            ('Катчхи','Катчхи'),
            ('Каннури','Каннури'),
            ('Кахетинская','Кахетинская'),
            ('Кашгарская','Кашгарская'),
            ('Караманская','Караманская'),
            ('Кулюкская','Кулюкская'),
            ('Кунальская','Кунальская'),
            ('Каргалинская','Каргалинская'),
            ('Ламанча','Ламанча'),
            ('Лаконская','Лаконская'),
            ('Латвийская','Латвийская'),
            ('Лесная','Лесная'),
            ('Левантинская','Левантинская'),
            ('Литовская белая','Литовская белая'),
            ('Липицкая','Липицкая'),
            ('Лал','Лал'),
            ('Лабитанская','Лабитанская'),
            ('Ларистанская','Ларистанская'),
            ('Ламбрук','Ламбрук'),
            ('Лакская','Лакская'),
            ('Линда','Линда'),
            ('Мурсийская','Мурсийская'),
            ('Мехсана','Мехсана'),
            ('Малагская','Малагская'),
            ('Матти','Матти'),
            ('Манипурская','Манипурская'),
            ('Мозамбикская','Мозамбикская'),
            ('Мальтийская','Мальтийская'),
            ('Монгольская','Монгольская'),
            ('Мегрельская','Мегрельская'),
            ('Морская','Морская'),
            ('Маарда','Маарда'),
            ('Мандаре','Мандаре'),
            ('Мбути','Мбути'),
            ('Минусинская','Минусинская'),
            ('Мангала','Мангала'),
            ('Мура','Мура'),
            ('Майпурская','Майпурская'),
            ('Миньянская','Миньянская'),
            ('Миау','Миау'),
            ('Мусала','Мусала'),
            ('Нагрийская','Нагрийская'),
            ('Нигерийская карликовая','Нигерийская карликовая'),
            ('Нубийская','Нубийская'),
            ('Непальская','Непальская'),
            ('Норвежская','Норвежская'),
            ('Нанги','Нанги'),
            ('Нанггинг','Нанггинг'),
            ('Нум','Нум'),
            ('Н’Гала','Н’Гала'),
            ('Оберхазли','Оберхазли'),
            ('Оренбургская','Оренбургская'),
            ('Оахская','Оахская'),
            ('Орловская','Орловская'),
            ('Одишанская','Одишанская'),
            ('Окахаи','Окахаи'),
            ('Олимбикская','Олимбикская'),
            ('Ошская','Ошская'),
            ('Овчепольская','Овчепольская'),
            ('Пуштунская','Пуштунская'),
            ('Пиренейская','Пиренейская'),
            ('Пакистанская','Пакистанская'),
            ('Придонская','Придонская'),
            ('Пенджабская','Пенджабская'),
            ('Пуатевинская','Пуатевинская'),
            ('Пейнт','Пейнт'),
            ('Панджа','Панджа'),
            ('Парват','Парват'),
            ('Персидская','Персидская'),
            ('Пиндская','Пиндская'),
            ('Пьянская','Пьянская'),
            ('Польская','Польская'),
            ('Полоцкая','Полоцкая'),
            ('Российская пуховая','Российская пуховая'),
            ('Резенская','Резенская'),
            ('Ровигна','Ровигна'),
            ('Российская горная','Российская горная'),
            ('Романская','Романская'),
            ('Раджстхани','Раджстхани'),
            ('Риби','Риби'),
            ('Раику','Раику'),
            ('Рама','Рама'),
            ('Рат','Рат'),
            ('Рупская','Рупская'),
            ('Регенская','Регенская'),
            ('Ронская','Ронская'),
            ('Салерно','Салерно'),
            ('Санкхен','Санкхен'),
            ('Савойская','Савойская'),
            ('Сирийская','Сирийская'),
            ('Саби','Саби'),
            ('Сардинская','Сардинская'),
            ('Сицилийская','Сицилийская'),
            ('Сокото','Сокото'),
            ('Сурати','Сурати'),
            ('Сахель','Сахель'),
            ('Саниенская','Саниенская'),
            ('Сарда','Сарда'),
            ('Севернокавказская','Севернокавказская'),
            ('Сен-Гейн','Сен-Гейн'),
            ('Свадебная','Свадебная'),
            ('Синди','Синди'),
            ('Севастопольская','Севастопольская'),
            ('Сакар','Сакар'),
            ('Сум','Сум'),
            ('Симба','Симба'),
            ('Скриери','Скриери'),
            ('Тоггенбургская ','Тоггенбургская'),
            ('Телинская','Телинская'),
            ('Тувинская','Тувинская'),
            ('Туркменская','Туркменская'),
            ('Тайская','Тайская'),
            ('Тибетская','Тибетская'),
            ('Тракийская','Тракийская'),
            ('Татарская','Татарская'),
            ('Той','Той'),
            ('Тель','Тель'),
            ('Тари','Тари'),
            ('Теруй','Теруй'),
            ('Тамбукская','Тамбукская'),
            ('Танская','Танская'),
            ('Удмуртская','Удмуртская'),
            ('Узбекская','Узбекская'),
            ('Украинская белая','Украинская белая'),
            ('Уральская','Уральская'),
            ('Уфимская','Уфимская'),
            ('Укумбайская','Укумбайская'),
            ('Уссурийская','Уссурийская'),
            ('Финская','Финская'),
            ('Филиппинская','Филиппинская'),
            ('Фрибуржская','Фрибуржская'),
            ('Фалабелла','Фалабелла'),
            ('Хангайская','Хангайская'),
            ('Халкай','Халкай'),
            ('Хердская','Хердская'),
            ('Химачали','Химачали'),
            ('Ходжа','Ходжа'),
            ('Хинди','Хинди'),
            ('Хейхуа','Хейхуа'),
            ('Хевсурская','Хевсурская'),
            ('Хансунская','Хансунская'),
            ('Чаппара','Чаппара'),
            ('Черная бенгальская','Черная бенгальская'),
            ('Чигу','Чигу'),
            ('Чегетуйская','Чегетуйская'),
            ('Чумбе','Чумбе'),
            ('Читтагонгская','Читтагонгская'),
            ('Чилийская','Чилийская'),
            ('Черекская','Черекская'),
            ('Чаросская','Чаросская'),
            ('Швейцарская','Швейцарская'),
            ('Шандунская','Шандунская'),
            ('Ширазская','Ширазская'),
            ('Шами','Шами'),
            ('Шугнанская','Шугнанская'),
            ('Шерстистая кашмирская','Шерстистая кашмирская'),
            ('Шахджаханпурская','Шахджаханпурская'),
            ('Шубарская','Шубарская'),
            ('Шенгенская','Шенгенская'),
            ('Шефский','Шефский'),
            ('Эстонская','Эстонская'),
            ('Эльзасская','Эльзасская'),
            ('Эфиопская','Эфиопская'),
            ('Югославская','Югославская'),
            ('Южноафриканская','Южноафриканская'),
            ('Южная нубийская','Южная нубийская'),
            ('Южноалтайская','Южноалтайская'),
            ('Юньнаньская','Юньнаньская'),
            ('Южногреческая','Южногреческая'),
            ('Якутская','Якутская'),
            ('Ярославская','Ярославская'),
        ],
        'Парнокопытные-Буйволы': [
            ('Азиатский речной','Азиатский речной'),
            ('Африканский','Африканский'),
        ],
        'Парнокопытные-Дромедары': [
            ('Австралийский','Австралийский'),
            ('Африканский','Африканский'),
            ('Ближневосточный','Ближневосточный'),
        ],
        'Парнокопытные-Бактрианы': [
            ('Казахский','Казахский'),
            ('Калмыцкий','Калмыцкий'),
            ('Китайский','Китайский'),
            ('Монгольский','Монгольский'),
        ],
        'Парнокопытные-Ламы': [
            ('Кхара','Кхара'),
            ('Сульти','Сульти'),
            ('Чакку','Чакку'),
        ],
        'Парнокопытные-Альпаки': [
            ('Сури','Сури'),
            ('Уакайа','Уакайа'),
        ],
        'Парнокопытные-Северные олени': [
            ('Ненецкий','Ненецкий'),
            ('Чукотский','Чукотский'),
            ('Эвенский','Эвенский'),
            ('Эвенкийский','Эвенкийский'),
        ],
        'Непарнокопытные-Лошади': [
            ('Арабская','Арабская'),
            ('Английская чистокровная','Английская чистокровная'),
            ('Ахалтекинская','Ахалтекинская'),
            ('Англо-норманнская','Англо-норманнская'),
            ('Азербайджанская','Азербайджанская'),
            ('Бельгийская','Бельгийская'),
            ('Венгерская','Венгерская'),
            ('Йоркширская','Йоркширская'),
            ('Ольденбургская','Ольденбургская'),
            ('Першерон','Першерон'),
            ('Тракененская','Тракененская'),
        ],
        'Непарнокопытные-Ослы': [
            ('Домашний','Домашний'),
            ('Лошак','Лошак'),
            ('Мул','Мул'),
        ],
        'Непарнокопытные-Пони': [
            ('Американский','Американский'),
            ('Исландский','Исландский'),
            ('Миниатюрный','Миниатюрный'),
            ('Уэльский','Уэльский'),
            ('Фалабелла','Фалабелла'),
            ('Шведский','Шведский'),
            ('Шетландский','Шетладский'),
            ('Шотландский','Шотландский'),
        ],
        'Кролики': [
            ('Венский голубой','Венский голубой'),
            ('Белый великан','Белый великан'),
            ('Калифорнийский','Калифорнийский'),
            ('Новозеландский белый','Новозеландский белый'),
            ('Новозеландский красный','Новозеландский красный'),
            ('Серый великан','Серый великан'),
            ('Серебристый','Серебристый'),
            ('Советская шиншилла','Советская шиншилла'),
            ('Черно-бурый','Черно-бурый'),
        ],
        'Грызуны': [
            ('Хомяк', 'Хомяк'),
            ('Крыса', 'Крыса'),
            ('Морская свинка', 'Морская свинка'),
        ],
        'Фретка': [
            ('Обыкновенный','Обыкновенный'),
            ('Сиамский','Сиамский'),
            ('Митт','Митт'),
            ('Пайблд','Пайблд'),
            ('Альбинос','Альбинос'),
            ('Руан','Руан'),
        ],
        'Птицы-курообразные': [
            ('Адлерская серебристая', 'Адлерская серебристая'),
            ('Альтштайрер', 'Альтштайрер'),
            ('Бассэт', 'Бассэт'),
            ('Бедуин', 'Бедуин'),
            ('Вельзумер', 'Вельзумер'),
            ('Виандот', 'Виандот'),
            ('Гамбургская', 'Гамбургская'),
            ('Гудан', 'Гудан'),
            ('Делавэрская голубая', 'Делавэрская'),
            ('Донг-тао', 'Донг-тао'),
            ('Ереванская красная', 'Ереванская красная'),
            ('Ереванская пурпурная', 'Ереванская пурпурная'),
            ('Ереванская черная', 'Ереванская черная'),
            ('Загорская белая', 'Загорская белая'),
            ('Зундхаймер', 'Зундхаймер'),
            ('Ивановская бойцовая', 'Ивановская бойцовая'),
            ('Кабардинская', 'Кабардинская'),
            ('Лафлеш', 'Лафлеш'),
            ('Леггорн', 'Леггорн'),
            ('Маран', 'Маран'),
            ('Нагоя', 'Нагоя'),
            ('Онагадори', 'Онагадори'),
            ('Оравка', 'Оравка'),
            ('Орпингтон', 'Орпингтон'),
            ('Охики', 'Охики'),
            ('Падуан', 'Падуан'),
            ('Речицкая', 'Речицкая'),
        ],
        'Птицы-гусеобразные': [
            ('Арзамасская', 'Арзамасская'),
            ('Банатская белая', 'Банатская белая'),
            ('Венгерская местная', 'Венгерская местная'),
            ('Горьковская', 'Горьковская'),
            ('Джавахетская', 'Джавахетская'),
            ('Итальянская', 'Итальянская'),
            ('Калужская', 'Калужская'),
            ('Ландская', 'Ландская'),
            ('Оброшинская серая', 'Оброшинская серая'),
            ('Переяславская', 'Переяславская'),
            ('Рейнская', 'Рейнская'),
            ('Тулузская', 'Тулузская'),
        ],
        'Птицы-голубеобразные': [
            ('Аахенский дутыш', 'Аахенский дутыш'),
            ('Бернбургский трубач', 'Бернбургский трубач'),
            ('Ганноверский турман', 'Ганноверский турман'),
        ],
        'Рептилии': [
            ('Игуана', 'Игуана'),
            ('Удав', 'Удав'),
            ('Черепаха', 'Черепаха'),
        ],
        'Другое': [
            ('Другое', 'Другое'),
        ],
    }
    
    SIZE_CHOICES = [
        ('Крупный', 'Крупный'),
        ('Средний', 'Средний'),
        ('Мелкий', 'Мелкий'),
    ]
    
    GENDER_CHOICES = [
        ('Мужской','Мужской'),
        ('Женский','Женский'),
    ]
    
    shelter = models.ForeignKey(Shelter, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    family = models.CharField(max_length=50, choices=FAMILY_CHOICES)
    breed = models.CharField(max_length=255, choices=BREED_CHOICES)
    gender = models.CharField(max_length=50,choices=GENDER_CHOICES)
    size = models.CharField(max_length=50, choices=SIZE_CHOICES)
    arrival_date = models.DateField()
    photo = models.ImageField(upload_to='pet_photos/', blank=True, null=True)
    vet_assignments = models.ManyToManyField('VetAssignment', through='PetVetAssignment', related_name='pets')
    
    def __str__(self):
        return self.name
    
    
class PetVetAssignment(models.Model):
    pet = models.ForeignKey('Pet', on_delete=models.CASCADE)
    vet_assignment = models.ForeignKey('VetAssignment', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('pet', 'vet_assignment')
        