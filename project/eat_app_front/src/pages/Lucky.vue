<template>
    <div v-if="isData === true">
        <NavBar/>
        <h1 class="page_category">Режим "Мне повезет"</h1>
        <div class="block_content">
            <div class="d-flex flex-row">
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

                    <div class="dish_count">
                        <button class="count_button" @click="incrementCountDishChoice(this.dish_count_choice)">+</button>
                        <p>Кол-во блюд: {{ this.dish_count_choice }}</p>
                        <button class="count_button" @click="decrementCountDishChoice(this.dish_count_choice)">-</button>
                    </div>

                    <button @click="get_random_order">Мне повезет</button>
                    <div class="primary_button">
                        <button class="bg-primary text-white" v-if="this.dish_posts.length" @click="sendUsersChoice">Заказать</button>
                    </div>
                </form>

                <div class="p-2">
                    <div class="dish_posts">
                        <div v-for="(dish, index) in dish_posts" :key="index">
                            <div class="dish">
                                <div class="dish_name"><h3>Название блюда: <br/> {{ dish.dish_name }}</h3></div>
                                <div><h4>Цена блюда: {{ dish.dish_price }}₽</h4></div>
                                <div class="dish_count">
                                    <div>Кол-во: {{ dish.dish_count }} &nbsp&nbsp</div>
                                    <button class="count_button" @click="incrementCountDish(index)">+</button>
                                    <button class="count_button" @click="decrementCountDish(index)">-</button>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <div v-else>
        <h1>Page not found</h1>
    </div>
</template>

<script>
import NavBar from "@/Components/NavBar.vue";
import axios from "axios";

export default {
    components: {NavBar},
    data() {
        return {
            users: [],
            dish_posts: [],
            selectedUser: null,
            max_dish_count: null,
            dish_count_choice: 1,
            selectedDate: null,
            isData: true,
        }
    },
    mounted() {
        axios.get('http://127.0.0.1:8000/api/user_view/')
            .then(response => {
                this.users = response.data
            })
            .catch(error => {
                console.log(error);
                self.isData = false
            })

        axios.get('http://127.0.0.1:8000/api/dish_view/')
            .then(response => {
                this.max_dish_count = response.data.length
            })
            .catch(error => {
                console.log(error)
            })
    },
    methods: {
        incrementCountDishChoice(){
            if (this.dish_count_choice < this.max_dish_count){
                this.dish_count_choice += 1;
            }
        },
        decrementCountDishChoice() {
            if (this.dish_count_choice > 1){
                this.dish_count_choice -= 1;
          }
        },
        get_random_order(){
            axios.post('http://127.0.0.1:8000/api/random_dish/', {'dish_count_choice': this.dish_count_choice})
                .then(response => {
                    this.dish_posts = response.data.dish_list
                })
                .catch(error => {
                    console.log(error)
                })
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

    },
}
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