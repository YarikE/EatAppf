<template xmlns="http://www.w3.org/1999/html">
    <NavBar/>
    <h1 class="page_category">Отчет "Заказы по дате"</h1>
    <div class="block_content">
        <div class="form_block">
            <input type="date" v-model="selectedDate">
            <button @click="getDateReport(selectedDate)">Сформировать отчет за дату</button>
        </div>

        <div class="table_block">
          <table class="order_table">
              <thead>
              <tr>
                  <th>Название</th>
                  <th>Количество</th>
                  <th>Цена в момент заказа</th>
                  <th>Общая стоимость</th>
              </tr>
              </thead>
              <tbody>
              <tr v-for="(dish_info, dish_name, index) in orderData" :key="index">
                  <td>{{ dish_name }}</td>
                  <td>{{ dish_info.dish_count }}</td>
                  <td>{{ dish_info.dish_now_price }}</td>
                  <td>{{ dish_info.dish_count * dish_info.dish_now_price }}</td>
              </tr>
              </tbody>
          </table>
          <p>Общая стоимость: {{ total }}</p>
        </div>
    </div>
</template>

<script>
import NavBar from "@/Components/NavBar.vue";
import axios from "axios";

export default {
    components: {NavBar},
    data() {
        return{
            selectedDate: null,
            orderData: {},
        }
    },
    methods: {
      getDateReport(date) {
          if (date != null){
              axios.post('http://127.0.0.1:8000/api/report/', {'data_choice': date})
                  .then(response => {
                      console.log(response.data)
                      this.orderData = response.data
                  })
                  .catch(error => {
                      console.log(error)
                  })
          } else {
              alert('Вы не выбрали дату!\nВыберите дату, пожалуйста :)')
          }
      }
    },
    computed: {
        total() {
            return Object.values(this.orderData).reduce((sum, dish) => sum + (dish.dish_count * dish.dish_now_price), 0);
        }
    }
}
</script>

<style lang="scss" scoped>

.order_table{
  border: 3px solid #000;
}

th, td {
  border: 2px solid #b8b8b8;
}

th {
  font-size: large;
}

.table_block{
  margin-top: 3%;
}
</style>