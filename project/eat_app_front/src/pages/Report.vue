<template>
    <div v-if="isData === true">
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
                <tr class="order_table_head">
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
        return{
            selectedDate: null,
            orderData: {},
            isData: true,
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
                      self.isData = false
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
  border: 2px solid #000;
}

th, td {
  border: 1px solid #b8b8b8;
  text-align: center;
}

th {
  font-size: large;
  padding: 4px;
}


.table_block{
  margin-top: 3%;
}

.order_table_head {
    font-family: 'Roboto Condensed', sans-serif;
}
</style>