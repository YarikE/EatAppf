<template>
    <NavBar/>
    <h1 class="page_category">Меню</h1>
    <ul>
        <li class="dish_element" v-for="elem in dishes" :key="elem.id">
            <div class="dish_name"><h2>{{elem.dish_name}}</h2></div>
            <div class="dish_compose">{{elem.dish_compose}}</div>
            <div class="dish_price"><h3>{{elem.dish_price}} руб.</h3></div>
            <div class="line"></div>
        </li>
    </ul>
</template>

<script>
import NavBar from "@/Components/NavBar.vue";
import axios from "axios";

export default {
    data() {
        return {
            dishes: [],
        };
    },
    mounted() {
        axios.get('http://127.0.0.1:8000/api/dish_view/')
            .then(response => {
                this.dishes = response.data
            })
            .catch(error => {
                console.log(error);
            });
    },
    components: {NavBar},
}

</script>

<style lang="scss">


</style>