'use client'

import { Button } from "@/components/ui/button"
import { Separator } from "@/components/ui/separator"
import { Plus } from "lucide-react"
import { useRouter, useParams } from "next/navigation"

import Heading from "@/components/ui/Heading"
import { DataTable } from "@/components/ui/DataTable"
import { CategoryColumn, columns } from "./Columns"
import ApiList from "@/components/ui/api.list"
import { ScrollArea } from "@/components/ui/scroll-area"

type Props = {
    categories: CategoryColumn[]
}

const CategoryClient = ({ categories }: Props) => {

    const router = useRouter()
    const params = useParams()
    return (
        <div className='h-full'>
            <div className="flex w-full justify-between items-center bg-muted/80 dark:bg-muted/50  px-2  py-1">
                <Heading
                    title={`Categories (${categories?.length})`}
                    description="Manage categories for your store"
                />
                <Button onClick={() => {
                    router.push(`/${params.storeId}/categories/new`)
                }}>
                    <Plus className="mr-2 h-4 w-4" />
                    Add New
                </Button>
            </div>
            <Separator className="mb-2"/>
            <ScrollArea className='h-full px-2'>
                <div className="bg-gradient-to-b  from-muted/20 to-muted/50 rounded-sm">
                    <DataTable columns={columns} data={categories} searchKey="name" />
                </div>
                <Heading title="API" description="API calls for Category" />
                <Separator />
                <ApiList entityName="categories" entityIdName="categoryId" />
                <div className='mb-20'/>
            </ScrollArea>
        </div>
    )
}

export default CategoryClient