import { StatusBar } from 'expo-status-bar';
import { useState } from 'react';
import { StyleSheet, Text, View, Button, FlatList } from 'react-native';
import ListingComponent from './components/ListingComponent';
import LaundryClothComponent from './components/LaundryClothComponent';



export default function App() {
  const [data, setData] = useState([
    { id: 1, name: 'Hello 1' },
    { id: 2, name: 'Hello 2' },
    { id: 3, name: 'Hello 3' },
    { id: 4, name: 'Hello 4' },
    { id: 5, name: 'Hello 5' },
  ])

  return (
    <View style={styles.container}>
      <Text>HEllo</Text>
      <LaundryClothComponent />
      
      <FlatList
        data={data}
        renderItem={
          ({item}) => (
            <Text>{item.name}</Text>
          )
        }
      />
        
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    paddingVertical: 13,
    // justifyContent: 'center',
  },
});
