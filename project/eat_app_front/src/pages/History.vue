<template>
    <NavBar/>
    <h1 class="page_category">История заказов</h1>
    <div class="block_content">
        <div class="select_user">
            <div>Выберите сотрудника из списка: </div>
            <select v-model="selectedUser">
                <option v-for="user in users" v-bind:value="user.user_name">{{user.user_name}}</option>
            </select>
            <button class="bg-primary text-white" @click="getHistory(selectedUser)">Выбрать сотрудника</button>
        </div>

        <div class="posts">
            <div v-for="(orders, index) in ordersData" :key="index">
                <div class="dish_element" v-for="(order, index) in orders" :key="index">
                    <h3>Дата заказа: {{ order.order_date }}</h3>
                    <div v-for="dish in order.dishes">
                        <div class="dish_in_order">
                            <div>Название блюда: {{ dish.dish_name }}</div>
                            <div>Кол-во: {{ dish.dish_count }}</div>
                            <div>Цена на момент заказа: {{ dish.dish_now_price }}</div>
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
    components: {NavBar},
    data(){
        return{
            selectedUser: null,
            users: [],
            ordersData: {},
        }
    },
    mounted() {
        axios.get('http://127.0.0.1:8000/api/user_view/')
            .then(response => {
                this.users = response.data
            })
            .catch(error => {
                console.log(error)
            })
    },
    methods: {
        getHistory(user) {
            axios.post('http://127.0.0.1:8000/api/history/', {user_name: user})
                .then(response =>{
                    console.log(response.data)
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

</style>