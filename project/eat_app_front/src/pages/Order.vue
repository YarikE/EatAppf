<template>
    <NavBar/>
    <h1 class="page_category">Заказ</h1>
    <div class="block_content">
        <div class="d-flex">
            <form @submit.prevent class="align-self-start">
                <div class="select_user">
                    <p>Выберите сотрудника:&nbsp</p>
                    <select v-model="selectedUser">
                        <option v-for="user in users" v-bind:value="user.user_name">{{user.user_name}}</option>
                    </select>
                </div>

                <div class="select_data">
                    <p>Выберите дату заказа:&nbsp</p>
                    <input type="date" v-model="selectedDate">
                </div>

                <div class="select_dish">
                    <p>Выберите блюдо:&nbsp</p>
                    <select v-model="selectedDish" id="dish_item">
                        <option disabled value="">Выберите товар</option>
                        <option v-for="dish in dishes" :key="dish.pk" :value="dish.dish_name">
                            {{ dish.dish_name }}
                        </option>
                    </select>
                    <span v-if="selectedDish">&nbsp&nbsp{{ dishes.find(dish => dish.dish_name === selectedDish).dish_price }}₽</span>
                    <div v-if="selectedDish" class="compound">Состав: <br/> {{ dishes.find(dish => dish.dish_name === selectedDish).dish_compose }}</div>
                </div>

                <button @click="addDishPost">Добавить блюдо</button>
                <div class="primary_button">
                    <button class="bg-primary text-white" v-if="this.dish_posts.length" @click="sendUsersChoice">Заказать</button>
                </div>
            </form>
            <div class="p-2" v-if="this.dish_posts.length">
                <div class="dish_posts">
                    <div v-for="(dish, index) in dish_posts" :key="index">
                        <div class="dish">
                            <div class="dish_name"><h4>Название блюда: <br/> {{ dish.dish_name }}</h4></div>
                            <div>Цена блюда: {{ dish.dish_price }}₽</div>
                            <div class="dish_count">
                                <div>Кол-во: {{ dish.dish_count }}</div>
                                <button class="count_button" @click="incrementCountDish(index)">+</button>
                                <button class="count_button" @click="decrementCountDish(index)">-</button>
                            </div>
                            <div>
                                <button class="bg-light text-dark" @click="deleteDishPost(index)">Удалить товар</button>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import NavBar from "@/Components/NavBar.vue";
import axios from "axios";

export default {
    data() {
        return {
            users: [], //users из API
            dishes: [], //dish из API
            selectedUser: null, // выбранный user из выпадающего списка
            selectedDish: null, // выбранное dish из выпадающего списка
            selectedDate: null, // выбранная дата из input'а с датой
            dish_posts: [], // список блюд
        };
    },

    mounted() {
        axios.get('http://127.0.0.1:8000/api/user_view/')
            .then(response => {
                this.users = response.data
            })
            .catch(error => {
                console.log(error);
        })
        axios.get('http://127.0.0.1:8000/api/dish_view/')
            .then(response => {
                this.dishes = response.data
            })
            .catch(error => {
                console.log(error)
            })
    },
    components: {NavBar},
    methods: {
        addDishPost() {
            if (this.selectedDish != null){
                if (this.dish_posts.some(item => item.dish_name === this.selectedDish) === false) {
                    this.dish_posts.push({
                        dish_name: this.dishes.find(item => item.dish_name === this.selectedDish)['dish_name'],
                        dish_compose: this.dishes.find(item => item.dish_name === this.selectedDish)['dish_compose'],
                        dish_price: this.dishes.find(item => item.dish_name === this.selectedDish)['dish_price'],
                        pk: this.dishes.find(item => item.dish_name === this.selectedDish)['pk'],
                        dish_count: 1,
                    })
                } else{
                    alert('Вы уже добавили этот товар')
                }
            }else{
                alert('Вы не добавили блюдо')
            }
        },
        deleteDishPost(index) {
            this.dish_posts.splice(index, 1)
        },
        incrementCountDish(index) {
            this.dish_posts[index].dish_count += 1
        },
        decrementCountDish(index) {
            if (this.dish_posts[index].dish_count >= 2){
                this.dish_posts[index].dish_count -= 1
            }
        },

        sendUsersChoice() {
            if (this.dish_posts.length > 0 && this.selectedUser != null && this.selectedDate != null){
                axios.post('http://127.0.0.1:8000/api/put_users_choice/', {
                    'user_name': this.selectedUser,
                    'dish_list': this.dish_posts,
                    'order_date': this.selectedDate
                })
                    .then(response => {
                        console.log(response)
                        console.log('Все норм :)')
                    })
                    .catch(error => {
                        console.log(error)
                    })
                alert('Вы успешно оформили заказ :)')
                location.reload();
            }else{
                alert('Вы ввели не все данные.\nПожалуйста, проверьте форму на заполнение всех данных')
            }
        },
    }
};
</script>

<style lang="scss" scoped>

.dish_name{
    white-space: nowrap;
    word-wrap: break-word;
}
.compound{
    margin-top: 10px;
    width: 170px;
    height: auto;
    word-wrap: break-word;
}

.align-self-start{
    border: 2px solid rgb(16, 127, 179);
    border-radius: 25px;
    padding: 15px;

}

.d-flex flex-row{
    align-items: flex-start;    
}
</style>