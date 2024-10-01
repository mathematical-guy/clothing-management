import { View, Text } from 'react-native'
import React from 'react'

export default function ListingComponent({data}) {
  return (
    <View>
      {
        data.map((item) => {
          return (
            <View key={item.id}>
              <Text>{item.name}</Text>
            </View>
          )
        })
      }
    </View>
  )
}