<template>
    <div v-if="isData === true">
        <NavBar/>
        <h1 class="page_category">История заказов</h1>
        <div class="block_content">
            <div class="select_user">
                <div>Выберите сотрудника из списка: </div>
                <select v-model="selectedUser" class="px-5">
                    <option v-for="user in users" v-bind:value="user.user_name">{{user.user_name}}</option>
                </select>
                <button class="bg-primary text-white" @click="getHistory(selectedUser)">Выбрать сотрудника</button>
            </div>

            <div class="posts">
                <div v-for="(orders, index) in ordersData" :key="index">
                    <div class="dish_history_element" v-for="(order, index) in orders" :key="index">
                        <h3 class="dish_date">Дата заказа: {{ order.order_date }}</h3>
                        <div v-for="dish in order.dishes">
                            <div class="dish_in_order">
                                <div>Название блюда:<p class="dish_history_name">{{ dish.dish_name }}</p></div>
                                <div>Кол-во: {{ dish.dish_count }}</div>
                                <div>Цена на момент заказа: <h5 class="dish_price">{{ dish.dish_now_price }} ₽</h5></div>
                            </div>
                        </div>
                        <div class="line"></div>
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
    data(){
        return{
            selectedUser: null,
            users: [],
            ordersData: {},
            isData: true,
        }
    },
    mounted() {
        axios.get('http://127.0.0.1:8000/api/user_view/')
            .then(response => {
                this.users = response.data
            })
            .catch(error => {
                console.log(error)
                this.isData = false
            })
    },
    methods: {
        getHistory(user) {
            axios.post('http://127.0.0.1:8000/api/history/', {user_name: user})
                .then(response =>{
                    this.ordersData = response.data
                })
                .catch(error => {
                    console.log(error)
                })
        }
    }

}
</script>

<style lang="scss" scoped>

.line {
    border-bottom: 2px solid grey;
    margin-bottom: 20px;
}

.dish_in_order{
    border: 1px solid grey;
    border-radius: 10px;
    padding: 5px;
}

.dish_date {
    font-family: 'Roboto Condensed', sans-serif;
}

.dish_history_name {
    font-family: 'Roboto Condensed', sans-serif;
}

</style>